extends CanvasLayer
class_name RecorderHUD

@export var player_path: NodePath
@export var objective_prefix := "OBJECTIVE  "
@export var compact_hints := false
@export var teach_legacy_play_key := true
@export var minimal_context_hints := false
@export var state_color_emphasis := false

const REC_HUD_COLOR := Color(0.86, 0.22, 0.15, 1.0)
const PLAY_HUD_COLOR := Color(0.90, 0.82, 0.67, 0.92)
const STOP_HUD_COLOR := Color(0.72, 0.65, 0.55, 0.58)

var player: MaloController
var recorder: Recorder
var _interaction_prompt := ""
var _last_status := ""
var _status_timeout := 0.0
var _has_clip := false
var _current_state := Recorder.State.STOP

@onready var objective_label: Label = $Margin/VBox/Objective
@onready var state_label: Label = $Margin/VBox/State
@onready var timer_label: Label = $Margin/VBox/Timer
@onready var hint_label: Label = $Margin/VBox/Hint
@onready var source_label: Label = $Margin/VBox/Source

func _ready() -> void:
    player = get_node(player_path) as MaloController
    player.recorder_equipped.connect(_on_recorder_equipped)
    player.nearby_source_changed.connect(_on_source_changed)
    player.interaction_prompt_changed.connect(_on_interaction_prompt_changed)
    player.recorder_action_rejected.connect(_on_action_rejected)
    _render_state(Recorder.State.STOP)
    timer_label.text = "00:00.0"
    source_label.text = "Source: —"
    _refresh_hint()

func set_objective(text: String) -> void:
    objective_label.text = "%s%s" % [objective_prefix, text]

func refresh_presentation() -> void:
    _render_state(_current_state)
    _refresh_hint()

func _process(delta: float) -> void:
    if _status_timeout <= 0.0:
        return
    _status_timeout = maxf(0.0, _status_timeout - delta)
    if _status_timeout == 0.0:
        _last_status = ""
        _refresh_hint()

func _on_recorder_equipped(new_recorder: Recorder) -> void:
    recorder = new_recorder
    recorder.state_changed.connect(_render_state)
    recorder.recording_time_changed.connect(_render_time)
    recorder.playback_time_changed.connect(_render_time)
    recorder.clip_created.connect(_on_clip_created)
    _render_state(recorder.state)
    _refresh_hint()

func _on_source_changed(source: RecordableSource) -> void:
    source_label.text = "Source: —" if source == null else "Source: %s" % source.clip_title
    _refresh_hint()

func _on_interaction_prompt_changed(prompt: String) -> void:
    _interaction_prompt = prompt
    _refresh_hint()

func _render_state(state: Recorder.State) -> void:
    _current_state = state
    match state:
        Recorder.State.REC:
            state_label.text = "● REC"
            if state_color_emphasis:
                state_label.add_theme_color_override("font_color", REC_HUD_COLOR)
        Recorder.State.PLAY:
            state_label.text = "▶ PLAY"
            if state_color_emphasis:
                state_label.add_theme_color_override("font_color", PLAY_HUD_COLOR)
        _:
            state_label.text = "■ STOP"
            if state_color_emphasis:
                state_label.add_theme_color_override("font_color", STOP_HUD_COLOR)
    if is_node_ready():
        _refresh_hint()

func _render_time(seconds: float) -> void:
    var minutes := int(seconds) / 60
    var secs := fmod(seconds, 60.0)
    timer_label.text = "%02d:%04.1f" % [minutes, secs]

func _on_clip_created(clip: RecordingClip) -> void:
    _has_clip = true
    timer_label.text = "%s  •  %.1fs" % [clip.clip_name, clip.duration_seconds]
    _last_status = "Recording saved"
    _status_timeout = 1.5
    _refresh_hint()

func _on_action_rejected(reason: String) -> void:
    _last_status = reason
    _status_timeout = 1.5
    _refresh_hint()

func _refresh_hint() -> void:
    if not _last_status.is_empty():
        hint_label.text = _last_status
        return
    if not _interaction_prompt.is_empty():
        hint_label.text = ("E / click  %s" if compact_hints else "E / Left click  %s") % _interaction_prompt
        return
    if recorder == null:
        hint_label.text = "Find the Fisher Price"
        return

    if minimal_context_hints:
        if _current_state == Recorder.State.REC:
            hint_label.text = "Release R  Stop"
            return
        if _current_state == Recorder.State.PLAY:
            hint_label.text = "Playing…"
            return
        if _has_clip:
            hint_label.text = "Space  Play"
            return
        if player.nearby_source != null:
            hint_label.text = "Hold R  Record"
            return
        hint_label.text = "Find a sound"
        return

    var play_hint := "Space / P  PLAY latest" if teach_legacy_play_key else "Space  Play"
    if player.nearby_source != null:
        hint_label.text = ("Hold R  Record    •    %s" if compact_hints else "Hold R  REC    •    %s") % play_hint
    else:
        hint_label.text = ("Find a sound    •    %s" if compact_hints else "Approach a sound source    •    %s") % play_hint
