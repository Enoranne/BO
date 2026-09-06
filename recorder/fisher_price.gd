extends Interactable
class_name FisherPrice

enum DeviceState { PLACED, EQUIPPED, ACTIVE }

signal device_state_changed(state: DeviceState)

var device_state: DeviceState = DeviceState.PLACED
var _equipped := false

@onready var recorder: Recorder = $Recorder

func _ready() -> void:
    interaction_prompt = "Take Fisher Price"
    recorder.state_changed.connect(_on_recorder_state_changed)

func interact(actor: Node) -> void:
    if not can_interact(actor):
        return
    if actor.has_method("equip_recorder") and actor.equip_recorder(recorder):
        _equipped = true
        interaction_enabled = false
        visible = false
        monitoring = false
        monitorable = false
        _set_device_state(DeviceState.EQUIPPED)

func _on_recorder_state_changed(recorder_state: Recorder.State) -> void:
    if not _equipped:
        return
    if recorder_state == Recorder.State.STOP:
        _set_device_state(DeviceState.EQUIPPED)
    else:
        _set_device_state(DeviceState.ACTIVE)

func _set_device_state(new_state: DeviceState) -> void:
    if device_state == new_state:
        return
    device_state = new_state
    device_state_changed.emit(device_state)
