extends CharacterBody3D
class_name MaloController

signal recorder_equipped(recorder: Recorder)
signal nearby_source_changed(source: RecordableSource)
signal interaction_prompt_changed(prompt: String)
signal recorder_action_rejected(reason: String)

@export var move_speed := 3.2
@export var acceleration := 14.0

var equipped_recorder: Recorder
var nearby_source: RecordableSource
var _gravity: float = ProjectSettings.get_setting("physics/3d/default_gravity")

@onready var interaction_context: InteractionContext = $InteractionContext
@onready var visual_rig: PlaceholderHumanoid3D = get_node_or_null("VisualRig")
@onready var held_recorder_visual: FisherPriceVisual = get_node_or_null("HeldRecorderVisual")

func _ready() -> void:
    interaction_context.interactable_changed.connect(_on_interactable_changed)
    interaction_context.recordable_source_changed.connect(_on_recordable_source_changed)

func _physics_process(delta: float) -> void:
    if not is_on_floor():
        velocity.y -= _gravity * delta

    var input_vec := Input.get_vector("move_left", "move_right", "move_forward", "move_back")
    var direction := Vector3(input_vec.x, 0.0, input_vec.y)
    var target_x := direction.x * move_speed
    var target_z := direction.z * move_speed
    velocity.x = move_toward(velocity.x, target_x, acceleration * delta)
    velocity.z = move_toward(velocity.z, target_z, acceleration * delta)

    if direction.length_squared() > 0.01:
        rotation.y = lerp_angle(rotation.y, atan2(direction.x, direction.z), minf(1.0, 10.0 * delta))

    move_and_slide()

    if visual_rig != null:
        var horizontal_speed := Vector2(velocity.x, velocity.z).length()
        visual_rig.set_motion_amount(horizontal_speed / maxf(move_speed, 0.001))

func _unhandled_input(event: InputEvent) -> void:
    if event.is_action_pressed("interact"):
        interaction_context.interact_current()

    if event.is_action_pressed("record"):
        try_begin_recording()

    if event.is_action_released("record"):
        try_stop_recording()

    if event.is_action_pressed("play_recording"):
        try_play_latest()

func equip_recorder(recorder: Recorder) -> bool:
    if recorder == null or equipped_recorder != null:
        return false
    equipped_recorder = recorder
    equipped_recorder.action_rejected.connect(_on_recorder_action_rejected)
    if held_recorder_visual != null:
        held_recorder_visual.visible = true
        held_recorder_visual.bind_recorder(equipped_recorder)
    recorder_equipped.emit(recorder)
    return true

func try_begin_recording() -> bool:
    if equipped_recorder == null:
        recorder_action_rejected.emit("Take the Fisher Price first")
        return false
    if nearby_source == null:
        recorder_action_rejected.emit("Move closer to a sound source")
        return false
    return equipped_recorder.start_recording(nearby_source)

func try_stop_recording() -> RecordingClip:
    if equipped_recorder == null or equipped_recorder.state != Recorder.State.REC:
        return null
    return equipped_recorder.stop_recording()

func try_play_latest() -> bool:
    if equipped_recorder == null:
        recorder_action_rejected.emit("Take the Fisher Price first")
        return false
    return equipped_recorder.play_latest()

func _on_interactable_changed(_interactable: Interactable) -> void:
    interaction_prompt_changed.emit(interaction_context.get_current_prompt())

func _on_recordable_source_changed(source: RecordableSource) -> void:
    nearby_source = source
    nearby_source_changed.emit(nearby_source)

func _on_recorder_action_rejected(reason: String) -> void:
    recorder_action_rejected.emit(reason)
