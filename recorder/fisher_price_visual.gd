extends Node3D
class_name FisherPriceVisual

@export var body_color := Color(0.70, 0.60, 0.43, 1.0)
@export var panel_color := Color(0.36, 0.08, 0.07, 1.0)
@export var cassette_color := Color(0.12, 0.10, 0.08, 0.88)
@export var rec_light_color := Color(1.0, 0.12, 0.05, 1.0)
@export var visual_scale := 0.72

var recorder: Recorder
var _rec_light: MeshInstance3D

func _ready() -> void:
    if get_child_count() == 0:
        _build_placeholder()
    _set_rec_light(false)

func bind_recorder(value: Recorder) -> void:
    if recorder != null and recorder.state_changed.is_connected(_on_recorder_state_changed):
        recorder.state_changed.disconnect(_on_recorder_state_changed)
    recorder = value
    if recorder != null:
        recorder.state_changed.connect(_on_recorder_state_changed)
        _on_recorder_state_changed(recorder.state)
    else:
        _set_rec_light(false)

func is_rec_light_visible() -> bool:
    return _rec_light != null and _rec_light.visible

func _on_recorder_state_changed(state: Recorder.State) -> void:
    _set_rec_light(state == Recorder.State.REC)

func _set_rec_light(enabled: bool) -> void:
    if _rec_light != null:
        _rec_light.visible = enabled

func _build_placeholder() -> void:
    var body_material := _material(body_color)
    var panel_material := _material(panel_color)
    var cassette_material := _material(cassette_color)
    var rec_material := _material(rec_light_color, true)

    var body := BoxMesh.new()
    body.size = Vector3(0.62, 0.42, 0.24) * visual_scale
    _add_mesh("Body", body, body_material, Vector3.ZERO)

    var panel := BoxMesh.new()
    panel.size = Vector3(0.38, 0.29, 0.028) * visual_scale
    _add_mesh("CassettePanel", panel, panel_material, Vector3(0, 0, 0.132) * visual_scale)

    var window := BoxMesh.new()
    window.size = Vector3(0.22, 0.15, 0.018) * visual_scale
    _add_mesh("CassetteWindow", window, cassette_material, Vector3(0, 0, 0.151) * visual_scale)

    var handle := BoxMesh.new()
    handle.size = Vector3(0.44, 0.06, 0.07) * visual_scale
    _add_mesh("Handle", handle, body_material, Vector3(0, 0.25, 0) * visual_scale)

    var rec_light_mesh := SphereMesh.new()
    rec_light_mesh.radius = 0.035 * visual_scale
    rec_light_mesh.height = 0.07 * visual_scale
    _rec_light = _add_mesh("RecLight", rec_light_mesh, rec_material, Vector3(0.245, 0.135, 0.145) * visual_scale)

func _add_mesh(node_name: String, mesh: Mesh, material: StandardMaterial3D, local_position: Vector3) -> MeshInstance3D:
    var instance := MeshInstance3D.new()
    instance.name = node_name
    instance.mesh = mesh
    instance.material_override = material
    instance.position = local_position
    add_child(instance)
    return instance

func _material(color: Color, emissive := false) -> StandardMaterial3D:
    var material := StandardMaterial3D.new()
    material.albedo_color = color
    material.roughness = 0.88
    if emissive:
        material.emission_enabled = true
        material.emission = color
        material.emission_energy_multiplier = 2.2
    return material
