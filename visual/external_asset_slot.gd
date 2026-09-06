extends Node3D
class_name ExternalAssetSlot

## Reversible presentation-only slot for imported 3D assets.
## No gameplay system may depend on the presence of asset_scene.

@export var asset_scene: PackedScene
@export var target_size := Vector3(2.15, 0.65, 1.08)
@export var show_envelope_when_empty := true
@export var envelope_floor_aligned := true

var _asset_instance: Node3D
var _envelope: MeshInstance3D

func _ready() -> void:
    _build_envelope()
    _refresh_asset()

func _refresh_asset() -> void:
    if _asset_instance != null:
        _asset_instance.queue_free()
        _asset_instance = null

    if asset_scene != null:
        var instance := asset_scene.instantiate()
        if instance is Node3D:
            _asset_instance = instance as Node3D
            add_child(_asset_instance)
            if _envelope != null:
                _envelope.visible = false
            return

    if _envelope != null:
        _envelope.visible = show_envelope_when_empty

func _build_envelope() -> void:
    if _envelope != null:
        return
    var mesh := BoxMesh.new()
    mesh.size = target_size
    var material := StandardMaterial3D.new()
    material.albedo_color = Color(0.18, 0.40, 0.52, 0.20)
    material.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
    material.shading_mode = BaseMaterial3D.SHADING_MODE_UNSHADED
    _envelope = MeshInstance3D.new()
    _envelope.name = "TargetEnvelope"
    _envelope.mesh = mesh
    _envelope.material_override = material
    if envelope_floor_aligned:
        _envelope.position.y = target_size.y * 0.5
    add_child(_envelope)
