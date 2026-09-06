extends Node3D
class_name PlaceholderHumanoid3D

@export var stature := 1.45
@export var shirt_color := Color(0.56, 0.31, 0.12, 1.0)
@export var trousers_color := Color(0.20, 0.15, 0.12, 1.0)
@export var skin_color := Color(0.72, 0.53, 0.37, 1.0)
@export var hair_color := Color(0.16, 0.09, 0.05, 1.0)
@export var facing_offset_degrees := 0.0
@export var idle_sway_degrees := 1.1
@export var gait_amplitude_degrees := 22.0
@export var gait_frequency := 7.0

var motion_amount := 0.0
var _phase := 0.0
var _left_arm: Node3D
var _right_arm: Node3D
var _left_leg: Node3D
var _right_leg: Node3D

func _ready() -> void:
    if get_child_count() == 0:
        _build_placeholder()
    rotation_degrees.y = facing_offset_degrees

func _process(delta: float) -> void:
    if _left_arm == null:
        return

    var motion := clampf(motion_amount, 0.0, 1.0)
    _phase += delta * lerpf(1.35, gait_frequency, motion)

    var gait := sin(_phase) * deg_to_rad(gait_amplitude_degrees) * motion
    _left_arm.rotation.x = -gait
    _right_arm.rotation.x = gait
    _left_leg.rotation.x = gait
    _right_leg.rotation.x = -gait

    var idle_weight := 1.0 - motion
    rotation.z = sin(_phase * 0.42) * deg_to_rad(idle_sway_degrees) * idle_weight

func set_motion_amount(value: float) -> void:
    motion_amount = clampf(value, 0.0, 1.0)

func _build_placeholder() -> void:
    var scale_factor := stature / 1.45
    var shirt := _material(shirt_color)
    var trousers := _material(trousers_color)
    var skin := _material(skin_color)
    var hair := _material(hair_color)

    var torso_mesh := BoxMesh.new()
    torso_mesh.size = Vector3(0.42, 0.54, 0.24) * scale_factor
    _add_mesh(self, "Torso", torso_mesh, shirt, Vector3(0, 0.88, 0) * scale_factor)

    var hips_mesh := BoxMesh.new()
    hips_mesh.size = Vector3(0.36, 0.18, 0.23) * scale_factor
    _add_mesh(self, "Hips", hips_mesh, trousers, Vector3(0, 0.54, 0) * scale_factor)

    var head_mesh := SphereMesh.new()
    head_mesh.radius = 0.17 * scale_factor
    head_mesh.height = 0.34 * scale_factor
    _add_mesh(self, "Head", head_mesh, skin, Vector3(0, 1.28, 0) * scale_factor)

    var hair_mesh := BoxMesh.new()
    hair_mesh.size = Vector3(0.32, 0.12, 0.28) * scale_factor
    _add_mesh(self, "Hair", hair_mesh, hair, Vector3(0, 1.39, -0.015) * scale_factor)

    var nose_mesh := BoxMesh.new()
    nose_mesh.size = Vector3(0.055, 0.055, 0.09) * scale_factor
    _add_mesh(self, "FacingMarker", nose_mesh, skin, Vector3(0, 1.28, 0.17) * scale_factor)

    _left_arm = _build_limb("LeftArm", Vector3(-0.255, 1.08, 0) * scale_factor, 0.43 * scale_factor, 0.058 * scale_factor, shirt)
    _right_arm = _build_limb("RightArm", Vector3(0.255, 1.08, 0) * scale_factor, 0.43 * scale_factor, 0.058 * scale_factor, shirt)
    _left_leg = _build_limb("LeftLeg", Vector3(-0.105, 0.49, 0) * scale_factor, 0.47 * scale_factor, 0.07 * scale_factor, trousers)
    _right_leg = _build_limb("RightLeg", Vector3(0.105, 0.49, 0) * scale_factor, 0.47 * scale_factor, 0.07 * scale_factor, trousers)

    _add_foot(_left_leg, "LeftFoot", 0.47 * scale_factor, trousers)
    _add_foot(_right_leg, "RightFoot", 0.47 * scale_factor, trousers)

func _build_limb(node_name: String, pivot_position: Vector3, length: float, radius: float, material: StandardMaterial3D) -> Node3D:
    var pivot := Node3D.new()
    pivot.name = node_name
    pivot.position = pivot_position
    add_child(pivot)

    var limb_mesh := CylinderMesh.new()
    limb_mesh.top_radius = radius
    limb_mesh.bottom_radius = radius * 1.06
    limb_mesh.height = length
    limb_mesh.radial_segments = 8
    _add_mesh(pivot, "Mesh", limb_mesh, material, Vector3(0, -length * 0.5, 0))
    return pivot

func _add_foot(parent: Node3D, node_name: String, leg_length: float, material: StandardMaterial3D) -> void:
    var foot_mesh := BoxMesh.new()
    foot_mesh.size = Vector3(0.16, 0.10, 0.28) * (stature / 1.45)
    _add_mesh(parent, node_name, foot_mesh, material, Vector3(0, -leg_length, 0.07 * (stature / 1.45)))

func _add_mesh(parent: Node3D, node_name: String, mesh: Mesh, material: StandardMaterial3D, local_position: Vector3) -> MeshInstance3D:
    var instance := MeshInstance3D.new()
    instance.name = node_name
    instance.mesh = mesh
    instance.material_override = material
    instance.position = local_position
    parent.add_child(instance)
    return instance

func _material(color: Color) -> StandardMaterial3D:
    var material := StandardMaterial3D.new()
    material.albedo_color = color
    material.roughness = 0.92
    return material
