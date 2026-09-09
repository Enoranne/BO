extends GdUnitTestSuite

var recorder: Recorder
var source: RecordableSource


func before_test() -> void:
    recorder = auto_free(Recorder.new()) as Recorder
    var player := AudioStreamPlayer.new()
    player.name = "PlaybackPlayer"
    recorder.add_child(player)
    add_child(recorder)

    source = auto_free(RecordableSource.new()) as RecordableSource
    source.source_id = &"ronan_test"
    source.clip_title = "RonanTest"
    source.source_metadata = {"role": "brother", "prototype": true}
    source.audio_stream = load("res://audio/ronan_test.wav") as AudioStream
    add_child(source)


func after_test() -> void:
    if is_instance_valid(recorder):
        recorder.stop()


func test_initial_guards_reject_invalid_actions() -> void:
    assert_int(recorder.state).is_equal(Recorder.State.STOP)
    assert_bool(recorder.play_latest()).is_false()
    assert_bool(recorder.start_recording(null)).is_false()
    assert_int(recorder.clips.size()).is_equal(0)


func test_recording_creates_independent_clip_with_metadata() -> void:
    assert_bool(recorder.start_recording(source)).is_true()
    assert_int(recorder.state).is_equal(Recorder.State.REC)
    assert_bool(recorder.start_recording(source)).is_false()

    await get_tree().create_timer(0.08).timeout
    var clip := recorder.stop_recording()

    assert_bool(clip != null).is_true()
    assert_int(recorder.state).is_equal(Recorder.State.STOP)
    assert_int(recorder.clips.size()).is_equal(1)
    assert_bool(recorder.get_latest_clip() == clip).is_true()
    assert_str(String(clip.source_id)).is_equal("ronan_test")
    assert_str(clip.source_title).is_equal("RonanTest")
    assert_bool(clip.duration_seconds > 0.0).is_true()
    assert_bool(clip.created_unix_time > 0).is_true()
    assert_str(String(clip.metadata.get("role", ""))).is_equal("brother")
    assert_str(String(clip.metadata.get("source_id", ""))).is_equal("ronan_test")
    assert_bool(clip.is_playable()).is_true()


func test_latest_clip_enters_play_and_returns_to_stop() -> void:
    assert_bool(recorder.start_recording(source)).is_true()
    await get_tree().create_timer(0.08).timeout
    var clip := recorder.stop_recording()
    assert_bool(clip != null).is_true()

    assert_bool(recorder.play_latest()).is_true()
    assert_int(recorder.state).is_equal(Recorder.State.PLAY)
    assert_bool(recorder.play_latest()).is_false()

    await get_tree().create_timer(0.02).timeout
    assert_bool(recorder.get_playback_seconds() >= 0.0).is_true()

    recorder.stop()
    assert_int(recorder.state).is_equal(Recorder.State.STOP)
    assert_float(recorder.get_playback_seconds()).is_equal(0.0)


func test_recorder_contract_stays_decoupled_from_narrative_systems() -> void:
    var recorder_script := FileAccess.get_file_as_string("res://recorder/recorder.gd")

    assert_bool(not recorder_script.contains("Christmas1982Director")).is_true()
    assert_bool(not recorder_script.contains("quest")).is_true()
    assert_bool(not recorder_script.contains("InteractionContext")).is_true()
    assert_bool(not recorder_script.contains("CinematicCamera")).is_true()
