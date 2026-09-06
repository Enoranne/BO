extends Node
class_name Period1982SetDressing

## Visual-only detail layer for the Sprint 5.2 wrapper scene.
## Creates no collision shapes and never modifies gameplay nodes or blocking markers.

@export var root_path: NodePath = NodePath("..")
@export var apply_on_ready := true

const TRIM_CREAM: Material = preload("res://materials/period_1982/painted_trim_cream.tres")
const WOOD_DARK: Material = preload("res://materials/period_1982/wood_dark_varnished.tres")
const UPHOLSTERY: Material = preload("res://materials/period_1982/upholstery_brown_orange.tres")
const ORNAMENT_RED: Material = preload("res://materials/period_1982/ornament_muted_red.tres")

func _ready() -> void:
    if apply_on_ready:
        call_deferred("apply_set_dressing")

func apply_set_dressing() -> void:
    var root := get_node_or_null(root_path)
    if root == null:
        push_warning("Period1982SetDressing: root_path does not resolve: %s" % root_path)
        return
    if root.get_node_or_null("VisualSetDressing") != null:
        return

    var layer := Node3D.new()
    layer.name = "VisualSetDressing"
    root.add_child(layer)

    # Painted skirting boards: enough architectural detail to stop the room reading as boxes.
    _add_box(layer, "BackSkirting", Vector3(11.65, 0.20, 0.08), Vector3(0.0, 0.16, -3.88), TRIM_CREAM)
    _add_box(layer, "LeftSkirting", Vector3(0.08, 0.20, 7.55), Vector3(-5.88, 0.16, 0.0), TRIM_CREAM)
    _add_box(layer, "RightSkirting", Vector3(0.08, 0.20, 7.55), Vector3(5.88, 0.16, 0.0), TRIM_CREAM)

    # Fireplace mantel: visually anchors the dominant warm corner without changing collision.
    _add_box(layer, "FireplaceMantel", Vector3(2.72, 0.16, 0.72), Vector3(-4.55, 2.23, -3.25), WOOD_DARK)

    # Three soft back cushions break the sofa silhouette and improve depth from the fixed camera.
    _add_box(layer, "SofaCushionLeft", Vector3(0.82, 0.56, 0.18), Vector3(-0.77, 1.12, -2.58), UPHOLSTERY, Vector3(-7.0, -4.0, 4.0))
    _add_box(layer, "SofaCushionMid", Vector3(0.82, 0.56, 0.18), Vector3(0.25, 1.10, -2.57), UPHOLSTERY, Vector3(-5.0, 1.5, -2.0))
    _add_box(layer, "SofaCushionRight", Vector3(0.82, 0.56, 0.18), Vector3(1.27, 1.12, -2.58), UPHOLSTERY, Vector3(-7.0, 5.0, -4.0))

    # Sparse ornaments: enough to sell Christmas without turning the procedural tree into final art.
    var ornaments := [
        Vector3(3.75, 1.18, -2.10),
        Vector3(4.48, 1.28, -2.02),
        Vector3(4.08, 1.62, -1.98),
        Vector3(4.60, 1.83, -2.34),
        Vector3(3.87, 2.02, -2.28),
        Vector3(4.36, 2.30, -2.27),
    ]
    for i in ornaments.size():
        _add_sphere(layer, "TreeOrnament%02d" % i, 0.075, ornaments[i], ORNAMENT_RED)

func _add_box(parent: Node3D, node_name: String, size: Vector3, position: Vector3, material: Material, rotation_degrees := Vector3.ZERO) -> void:
    var mesh := BoxMesh.new()
    mesh.size = size
    var instance := MeshInstance3D.new()
    instance.name = node_name
    instance.mesh = mesh
    instance.material_override = material
    instance.position = position
    instance.rotation_degrees = rotation_degrees
    parent.add_child(instance)

func _add_sphere(parent: Node3D, node_name: String, radius: float, position: Vector3, material: Material) -> void:
    var mesh := SphereMesh.new()
    mesh.radius = radius
    mesh.height = radius * 2.0
    var instance := MeshInstance3D.new()
    instance.name = node_name
    instance.mesh = mesh
    instance.material_override = material
    instance.position = position
    parent.add_child(instance)
