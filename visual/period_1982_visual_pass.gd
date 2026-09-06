extends Node
class_name Period1982VisualPass

## Presentation-only material and readability override pass for the Sprint 5 vertical slice.
## It does not move gameplay nodes, alter collisions, or own gameplay state.

@export var root_path: NodePath = NodePath("..")
@export var apply_on_ready := true
@export var tune_lighting := true
@export var hide_debug_world_labels := true

const WALLPAPER_CREAM: Material = preload("res://materials/period_1982/wallpaper_cream.tres")
const WOOD_DARK_VARNISHED: Material = preload("res://materials/period_1982/wood_dark_varnished.tres")
const UPHOLSTERY_BROWN_ORANGE: Material = preload("res://materials/period_1982/upholstery_brown_orange.tres")
const CARPET_MUTED_BROWN: Material = preload("res://materials/period_1982/carpet_muted_brown.tres")
const FLOOR_DARK_WARM_BROWN: Material = preload("res://materials/period_1982/floor_dark_warm_brown.tres")
const FIREPLACE_STONE_WARM: Material = preload("res://materials/period_1982/fireplace_stone_warm.tres")
const FISHER_BEIGE: Material = preload("res://materials/period_1982/plastic_fisher_beige.tres")
const FISHER_BURGUNDY: Material = preload("res://materials/period_1982/plastic_fisher_burgundy.tres")
const FISHER_WINDOW_DARK: Material = preload("res://materials/period_1982/plastic_fisher_window_dark.tres")
const REC_BUTTON_RED: Material = preload("res://materials/period_1982/plastic_rec_red.tres")

func _ready() -> void:
    if apply_on_ready:
        call_deferred("apply_visual_pass")

func apply_visual_pass() -> void:
    var root := get_node_or_null(root_path)
    if root == null:
        push_warning("Period1982VisualPass: root_path does not resolve: %s" % root_path)
        return

    # Architecture / set surfaces.
    _override(root, "Set/Floor/Mesh", FLOOR_DARK_WARM_BROWN)
    _override(root, "Set/BackWall/Mesh", WALLPAPER_CREAM)
    _override(root, "Set/LeftWall/Mesh", WALLPAPER_CREAM)
    _override(root, "Set/RightWall/Mesh", WALLPAPER_CREAM)
    _override(root, "Set/RugPlaceholder", CARPET_MUTED_BROWN)

    # Furniture and fireplace.
    _override(root, "Set/SofaPlaceholder/Seat", UPHOLSTERY_BROWN_ORANGE)
    _override(root, "Set/SofaPlaceholder/Back", UPHOLSTERY_BROWN_ORANGE)
    _override(root, "Set/SofaPlaceholder/ArmLeft", UPHOLSTERY_BROWN_ORANGE)
    _override(root, "Set/SofaPlaceholder/ArmRight", UPHOLSTERY_BROWN_ORANGE)
    _override(root, "Set/CoffeeTablePlaceholder/Top", WOOD_DARK_VARNISHED)
    _override(root, "Set/CoffeeTablePlaceholder/LegFL", WOOD_DARK_VARNISHED)
    _override(root, "Set/CoffeeTablePlaceholder/LegFR", WOOD_DARK_VARNISHED)
    _override(root, "Set/CoffeeTablePlaceholder/LegBL", WOOD_DARK_VARNISHED)
    _override(root, "Set/CoffeeTablePlaceholder/LegBR", WOOD_DARK_VARNISHED)
    _override(root, "Set/TreePlaceholder/Trunk", WOOD_DARK_VARNISHED)
    _override(root, "Set/FireplacePlaceholder/Main", FIREPLACE_STONE_WARM)
    _override(root, "Set/FireplacePlaceholder/Hearth", FIREPLACE_STONE_WARM)

    # World Fisher Price placeholder: presentation-only detail layer.
    _override(root, "FisherPrice/Visual", FISHER_BEIGE)
    _ensure_world_fisher_details(root)

    # Sprint 4 carried Fisher Price builds its mesh children procedurally.
    _override(root, "Malo/HeldRecorderVisual/Body", FISHER_BEIGE)
    _override(root, "Malo/HeldRecorderVisual/Handle", FISHER_BEIGE)
    _override(root, "Malo/HeldRecorderVisual/CassettePanel", FISHER_BURGUNDY)
    _override(root, "Malo/HeldRecorderVisual/CassetteWindow", FISHER_WINDOW_DARK)

    if tune_lighting:
        _tune_lighting(root)
    if hide_debug_world_labels:
        _set_visible(root, "FisherPrice/Label", false)
        _set_visible(root, "RonanTest/Label", false)

func _tune_lighting(root: Node) -> void:
    var fire := root.get_node_or_null("Lighting/FireGlow") as OmniLight3D
    if fire != null:
        fire.light_energy = 3.7
        fire.omni_range = 5.8
        fire.light_color = Color(1.0, 0.38, 0.14, 1.0)

    var tree := root.get_node_or_null("Lighting/TreeLamp") as OmniLight3D
    if tree != null:
        tree.light_energy = 1.55
        tree.omni_range = 5.9
        tree.light_color = Color(1.0, 0.67, 0.40, 1.0)

    var fill := root.get_node_or_null("Lighting/SoftFill") as DirectionalLight3D
    if fill != null:
        fill.light_energy = 0.38
        fill.light_color = Color(1.0, 0.76, 0.58, 1.0)

func _ensure_world_fisher_details(root: Node) -> void:
    var fisher := root.get_node_or_null("FisherPrice") as Node3D
    if fisher == null or fisher.get_node_or_null("VisualDetails") != null:
        return

    var details := Node3D.new()
    details.name = "VisualDetails"
    fisher.add_child(details)

    _add_visual_box(details, "CassettePanel", Vector3(0.50, 0.31, 0.025), Vector3(0.0, 0.0, 0.202), FISHER_BURGUNDY)
    _add_visual_box(details, "CassetteWindow", Vector3(0.28, 0.17, 0.012), Vector3(0.0, 0.0, 0.221), FISHER_WINDOW_DARK)
    _add_visual_box(details, "Handle", Vector3(0.54, 0.07, 0.08), Vector3(0.0, 0.30, 0.0), FISHER_BEIGE)
    _add_visual_box(details, "PlayButton", Vector3(0.10, 0.045, 0.085), Vector3(0.11, 0.265, 0.08), FISHER_BURGUNDY)
    _add_visual_box(details, "RecButton", Vector3(0.10, 0.045, 0.085), Vector3(0.25, 0.265, 0.08), REC_BUTTON_RED)

func _add_visual_box(parent: Node3D, node_name: String, size: Vector3, position: Vector3, material: Material) -> void:
    var mesh := BoxMesh.new()
    mesh.size = size
    var instance := MeshInstance3D.new()
    instance.name = node_name
    instance.mesh = mesh
    instance.material_override = material
    instance.position = position
    parent.add_child(instance)

func _override(root: Node, relative_path: NodePath, material: Material) -> void:
    var node := root.get_node_or_null(relative_path)
    if node is MeshInstance3D:
        (node as MeshInstance3D).material_override = material

func _set_visible(root: Node, relative_path: NodePath, value: bool) -> void:
    var node := root.get_node_or_null(relative_path)
    if node is Node3D:
        (node as Node3D).visible = value
