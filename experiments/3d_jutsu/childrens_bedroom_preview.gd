extends Node3D

const ASSET_PATH := "res://assets/3d/experimental/childrens_bedroom_3d_jutsu.glb"
const CUTAWAY_NODE_NAMES := [
    "ROOM_ceil",
    "WALL_F1",
    "WALL_F2",
    "WALL_F3",
    "WALL_F4",
    "WALL_F5",
]

@export var camera_target := Vector3(4.0, 1.3, -3.5)
@export var cutaway_mode := true

@onready var asset_root: Node3D = $AssetRoot
@onready var preview_camera: Camera3D = $PreviewCamera
@onready var status_label: Label = $HUD/Margin/Status

func _ready() -> void:
    preview_camera.look_at(camera_target, Vector3.UP)
    _load_candidate()

func _load_candidate() -> void:
    if not ResourceLoader.exists(ASSET_PATH):
        status_label.text = "3D Jutsu bedroom: asset missing\nPlace childrens_bedroom_3d_jutsu.glb in assets/3d/experimental/"
        return

    var resource := load(ASSET_PATH)
    if not resource is PackedScene:
        status_label.text = "3D Jutsu bedroom: import is not a PackedScene"
        return

    var instance := (resource as PackedScene).instantiate()
    if not instance is Node3D:
        status_label.text = "3D Jutsu bedroom: imported root is not Node3D"
        instance.queue_free()
        return

    asset_root.add_child(instance)
    if cutaway_mode:
        _apply_cutaway(instance)

    status_label.text = "3D Jutsu bedroom — DIRECT GLB → GODOT\nCutaway review: scale, materials, hierarchy and misplaced transforms"

func _apply_cutaway(root_node: Node) -> void:
    for node_name in CUTAWAY_NODE_NAMES:
        var node := root_node.find_child(node_name, true, false)
        if node is Node3D:
            (node as Node3D).visible = false
