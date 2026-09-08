extends SceneTree

var failures := 0
var playback_time_observed := 0.0

func _initialize() -> void:
    call_deferred("_run")

func _check(condition: bool, message: String) -> void:
    if condition:
        print("PASS: ", message)
    else:
        failures += 1
        push_error("FAIL: " + message)

func _on_playback_time_changed(seconds: float) -> void:
    playback_time_observed = maxf(playback_time_observed, seconds)

func _run() -> void:
    var recorder_scene := Recorder.new()
    var player := AudioStreamPlayer.new()
    player.name = "PlaybackPlayer"
    recorder_scene.add_child(player)
    root.add_child(recorder_scene)
    recorder_scene.playback_time_changed.connect(_on_playback_time_changed)

    var source := RecordableSource.new()
    source.source_id = &"ronan_test"
    source.clip_title = "RonanTest"
    source.source_metadata = {"role": "brother", "prototype": true}
    source.audio_stream = load("res://audio/ronan_test.wav")
    root.add_child(source)

    await process_frame

    _check(not recorder_scene.play_latest(), "PLAY fails cleanly when no clip exists")
    _check(not recorder_scene.start_recording(null), "REC rejects a missing source")
    _check(recorder_scene.start_recording(source), "Recorder enters REC with a valid source")
    _check(not recorder_scene.start_recording(source), "A second REC cannot start while already recording")

    await create_timer(0.15).timeout
    var clip := recorder_scene.stop_recording()
    _check(clip != null, "Stopping REC creates a RecordingClip")
    _check(recorder_scene.clips.size() == 1, "RecordingClip is stored independently")
    _check(clip.source_id == &"ronan_test", "RecordingClip preserves source id")
    _check(clip.source_title == "RonanTest", "RecordingClip preserves source title")
    _check(clip.duration_seconds > 0.0, "RecordingClip stores duration")
    _check(clip.created_unix_time > 0, "RecordingClip stores creation timestamp")
    _check(clip.metadata.get("role") == "brother", "RecordingClip preserves source metadata")
    _check(clip.is_playable(), "RecordingClip reports itself playable")

    playback_time_observed = -1.0
    _check(recorder_scene.play_latest(), "Latest RecordingClip can enter PLAY")
    _check(not recorder_scene.play_latest(), "PLAY cannot start twice simultaneously")
    await create_timer(0.05).timeout
    _check(playback_time_observed > 0.0, "PLAY emits elapsed playback time for presentation")
    _check(recorder_scene.get_playback_seconds() > 0.0, "Recorder exposes current playback elapsed time")
    recorder_scene.stop()
    _check(recorder_scene.state == Recorder.State.STOP, "Recorder returns to STOP")

    clip = null
    recorder_scene.queue_free()
    source.queue_free()
    await process_frame
    # Let the audio server retire stopped playback references before shutdown.
    await create_timer(0.1).timeout
    print("Recorder tests complete. Failures: ", failures)
    call_deferred("quit", failures)
