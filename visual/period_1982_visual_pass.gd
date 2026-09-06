extends Node
class_name Period1982VisualPass

## Presentation-only material override pass for the Sprint 5 vertical slice.
## It does not move nodes, alter collisions, or own gameplay state.

@export var root_path: NodePath = NodePath("..")
@export var apply_on_ready := true

const WALLPAPER_CREAM: Material = preload("res://materials/period_1982/wallpaper_cream.tres")
const WOOD_DARK_VARNISHED: Material = preload("res://materials/period_1982/wood_dark_varnished.tres")
const UPHOLSTERY_BROWN_ORANGE: Material = preload("res://materials/period_1982/upholstery_brown_orange.tres")
const CARPET_MUTED_BROWN: Material = preload("res://materials/period_1982/carpet_muted_brown.tres")
const FISHER_BEIGE: Material = preload("res://materials/period_1982/plastic_fisher_beige.tres")
const FISHER_BURGUNDY: Material = preload("res://materials/period_1982/plastic_fisher_burgundy.tres")

func _ready() -> void:
    if apply_on_ready:
        call_deferred("apply_visual_pass")

func apply_visual_pass() -> void:
    var root := get_node_or_null(root_path)
    if root == null:
        push_warning("Period1982VisualPass: root_path does not resolve: %s" % root_path)
        return

    # Architecture / set surfaces.
    _override(root, "Set/BackWall/Mesh", WALLPAPER_CREAM)
    _override(root, "Set/LeftWall/Mesh", WALLPAPER_CREAM)
    _override(root, "Set/RightWall/Mesh", WALLPAPER_CREAM)
    _override(root, "Set/RugPlaceholder", CARPET_MUTED_BROWN)

    # Furniture.
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

    # World Fisher Price placeholder.
    _override(root, "FisherPrice/Visual", FISHER_BEIGE)

    # Sprint 4 carried Fisher Price builds its mesh children procedurally.
    # Apply after _ready() has built them. Missing children are intentionally tolerated.
    _override(root, "Malo/HeldRecorderVisual/Body", FISHER_BEIGE)
    _override(root, "Malo/HeldRecorderVisual/Handle", FISHER_BEIGE)
    _override(root, "Malo/HeldRecorderVisual/CassettePanel", FISHER_BURGUNDY)

func _override(root: Node, relative_path: NodePath, material: Material) -> void:
    var node := root.get_node_or_null(relative_path)
    if node == null:
        return
    if node is MeshInstance3D:
        (node as MeshInstance3D).material_override = material
