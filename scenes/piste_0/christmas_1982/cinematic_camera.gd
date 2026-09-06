extends Camera3D

@export_node_path("Node3D") var target_path: NodePath
@export var follow_x := 0.18
@export var follow_z := 0.10
@export var max_offset := Vector2(0.95, 0.55)
@export var smoothing := 2.8
@export var focus_height := 0.9

var _camera_anchor: Vector3
var _target_anchor: Vector3
@onready var target: Node3D = get_node_or_null(target_path)

func _ready() -> void:
    _camera_anchor = global_position
    if target != null:
        _target_anchor = target.global_position
        _look_at_target()

func _process(delta: float) -> void:
    if target == null:
        return

    var displacement := target.global_position - _target_anchor
    var desired := _camera_anchor
    desired.x += clampf(displacement.x * follow_x, -max_offset.x, max_offset.x)
    desired.z += clampf(displacement.z * follow_z, -max_offset.y, max_offset.y)

    var weight := 1.0 - exp(-smoothing * delta)
    global_position = global_position.lerp(desired, weight)
    _look_at_target()

func _look_at_target() -> void:
    look_at(target.global_position + Vector3(0.0, focus_height, 0.0), Vector3.UP)
