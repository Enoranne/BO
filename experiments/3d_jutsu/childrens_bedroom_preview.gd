extends Node3D

const ASSET_PATH := "res://assets/3d/experimental/childrens_bedroom_3d_jutsu.glb"

@export var camera_target := Vector3(3.0, 1.0, -1.0)

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
    status_label.text = "3D Jutsu bedroom — DIRECT GLB → GODOT\nInspect scale, materials, hierarchy, pivots and camera framing"
