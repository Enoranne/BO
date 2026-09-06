extends Camera3D
class_name AssetPreviewCamera

@export var target_path: NodePath
@export var target_height := 0.40

func _ready() -> void:
    var target := get_node_or_null(target_path) as Node3D
    if target != null:
        look_at(target.global_position + Vector3(0.0, target_height, 0.0), Vector3.UP)
