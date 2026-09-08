extends Node
class_name Recorder

enum State { STOP, REC, PLAY }

signal state_changed(state: State)
signal recording_time_changed(seconds: float)
signal playback_time_changed(seconds: float)
signal clip_created(clip: RecordingClip)
signal action_rejected(reason: String)

@export_group("Capability profile")
@export var device_id: StringName = &"fisher_price"
@export var track_count: int = 1
@export var supports_pitch: bool = false
@export var supports_sound_on_sound: bool = false

var state: State = State.STOP
var clips: Array[RecordingClip] = []
var _recording_source: RecordableSource
var _recording_elapsed := 0.0
var _playback_elapsed := 0.0
var _playing_clip: RecordingClip

@onready var playback_player: AudioStreamPlayer = $PlaybackPlayer

func _process(delta: float) -> void:
    match state:
        State.REC:
            _recording_elapsed += delta
            recording_time_changed.emit(_recording_elapsed)
        State.PLAY:
            if _playing_clip == null:
                stop()
                return
            _playback_elapsed = minf(_playback_elapsed + delta, _playing_clip.duration_seconds)
            playback_time_changed.emit(_playback_elapsed)
            if _playback_elapsed >= _playing_clip.duration_seconds:
                stop()

func start_recording(source: RecordableSource) -> bool:
    if state != State.STOP:
        _reject("Recorder is busy")
        return false
    if source == null or not source.can_record():
        _reject("No recordable source")
        return false

    _recording_source = source
    _recording_elapsed = 0.0
    _set_state(State.REC)
    source.preview()
    return true

func stop_recording() -> RecordingClip:
    if state != State.REC or _recording_source == null:
        _reject("Recorder is not recording")
        return null

    var clip := RecordingClip.new()
    clip.clip_name = _recording_source.clip_title
    clip.source_id = _recording_source.source_id
    clip.source_title = _recording_source.clip_title
    clip.stream = _recording_source.get_recording_stream()
    clip.metadata = _recording_source.get_recording_metadata()
    clip.created_unix_time = int(Time.get_unix_time_from_system())

    var stream_length := clip.stream.get_length() if clip.stream != null else 0.0
    var captured := maxf(_recording_elapsed, 0.05)
    clip.duration_seconds = minf(captured, stream_length) if stream_length > 0.0 else captured
    clips.append(clip)

    _recording_source = null
    _recording_elapsed = 0.0
    _set_state(State.STOP)
    clip_created.emit(clip)
    return clip

func play_latest() -> bool:
    if clips.is_empty():
        _reject("No recording available")
        return false
    return play_clip(clips.back())

func play_clip(clip: RecordingClip) -> bool:
    if state != State.STOP:
        _reject("Recorder is busy")
        return false
    if clip == null or not clip.is_playable():
        _reject("Recording is not playable")
        return false

    _playing_clip = clip
    _playback_elapsed = 0.0
    playback_player.stream = clip.stream
    playback_player.play()
    _set_state(State.PLAY)
    playback_time_changed.emit(_playback_elapsed)
    return true

func stop() -> void:
    if state == State.REC:
        stop_recording()
        return
    if playback_player.playing:
        playback_player.stop()
    _playing_clip = null
    _playback_elapsed = 0.0
    _set_state(State.STOP)

func get_latest_clip() -> RecordingClip:
    return null if clips.is_empty() else clips.back()

func get_recording_seconds() -> float:
    return _recording_elapsed

func get_playback_seconds() -> float:
    return _playback_elapsed

func _set_state(new_state: State) -> void:
    if state == new_state:
        return
    state = new_state
    state_changed.emit(state)

func _reject(reason: String) -> void:
    action_rejected.emit(reason)
