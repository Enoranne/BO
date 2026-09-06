extends Node
class_name Christmas1982Director

enum Beat { FIND_FISHER, RECORD_RONAN, PLAY_RECORDING, COMPLETE }

signal beat_changed(beat: Beat)

@export var player_path: NodePath
@export var hud_path: NodePath

var beat: Beat = Beat.FIND_FISHER
var _recorder: Recorder
var _saw_playback := false

@onready var player: MaloController = get_node(player_path) as MaloController
@onready var hud: RecorderHUD = get_node(hud_path) as RecorderHUD

func _ready() -> void:
    player.recorder_equipped.connect(_on_recorder_equipped)
    call_deferred("_render_objective")

func _on_recorder_equipped(recorder: Recorder) -> void:
    _recorder = recorder
    if not _recorder.clip_created.is_connected(_on_clip_created):
        _recorder.clip_created.connect(_on_clip_created)
    if not _recorder.state_changed.is_connected(_on_recorder_state_changed):
        _recorder.state_changed.connect(_on_recorder_state_changed)
    _set_beat(Beat.RECORD_RONAN)

func _on_clip_created(clip: RecordingClip) -> void:
    if clip != null and clip.source_id == &"ronan_test":
        _saw_playback = false
        _set_beat(Beat.PLAY_RECORDING)

func _on_recorder_state_changed(state: Recorder.State) -> void:
    if beat != Beat.PLAY_RECORDING:
        return
    if state == Recorder.State.PLAY:
        _saw_playback = true
    elif state == Recorder.State.STOP and _saw_playback:
        _set_beat(Beat.COMPLETE)

func _set_beat(new_beat: Beat) -> void:
    if beat == new_beat:
        return
    beat = new_beat
    _render_objective()
    beat_changed.emit(beat)

func _render_objective() -> void:
    if hud == null:
        return
    match beat:
        Beat.FIND_FISHER:
            hud.set_objective("Find the Fisher Price")
        Beat.RECORD_RONAN:
            hud.set_objective("Record Ronan")
        Beat.PLAY_RECORDING:
            hud.set_objective("Play your recording")
        Beat.COMPLETE:
            hud.set_objective("First recording complete")
