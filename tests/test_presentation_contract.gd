extends SceneTree

var failures := 0

func _initialize() -> void:
    call_deferred("_run")

func _check(condition: bool, message: String) -> void:
    if condition:
        print("PASS: ", message)
    else:
        failures += 1
        push_error("FAIL: " + message)

func _run() -> void:
    var packed := load("res://scenes/piste_0/christmas_1982/Christmas1982.tscn") as PackedScene
    _check(packed != null, "Christmas1982 loads for presentation contract")
    if packed == null:
        quit(failures)
        return

    var scene := packed.instantiate()
    root.add_child(scene)
    await process_frame
    await physics_frame

    var malo := scene.get_node("Malo") as MaloController
    var held_visual := scene.get_node("Malo/HeldRecorderVisual") as FisherPriceVisual
    var fisher := scene.get_node("FisherPrice") as FisherPrice
    var ronan := scene.get_node("RonanTest") as RecordableSource
    var director := scene.get_node("Christmas1982Director") as Christmas1982Director
    var objective := scene.get_node("HUD/Margin/VBox/Objective") as Label

    _check(held_visual != null, "Malo has carried Fisher Price placeholder visual")
    _check(not held_visual.visible, "Carried Fisher Price starts hidden")
    _check(director.beat == Christmas1982Director.Beat.FIND_FISHER, "Director starts at FIND_FISHER")
    _check("Fisher" in objective.text, "HUD initially directs player to Fisher Price")

    fisher.interact(malo)
    await process_frame
    _check(held_visual.visible, "Taking Fisher Price reveals carried device")
    _check(held_visual.recorder == malo.equipped_recorder, "Carried visual binds to equipped Recorder")
    _check(director.beat == Christmas1982Director.Beat.RECORD_RONAN, "Pickup advances presentation beat to RECORD_RONAN")
    _check("Ronan" in objective.text, "HUD objective advances to Ronan")

    malo.nearby_source = ronan
    _check(malo.try_begin_recording(), "Presentation contract can start REC")
    await process_frame
    _check(held_visual.is_rec_light_visible(), "Carried Fisher Price REC light is visible during REC")

    await create_timer(0.12).timeout
    var clip := malo.try_stop_recording()
    await process_frame
    _check(clip != null, "Presentation contract creates Ronan clip")
    _check(not held_visual.is_rec_light_visible(), "REC light switches off after STOP")
    _check(director.beat == Christmas1982Director.Beat.PLAY_RECORDING, "Recording advances presentation beat to PLAY_RECORDING")
    _check("Play" in objective.text, "HUD asks player to play recording")

    _check(malo.try_play_latest(), "Presentation contract can PLAY latest clip")
    await process_frame
    malo.equipped_recorder.stop()
    await process_frame
    _check(director.beat == Christmas1982Director.Beat.COMPLETE, "Completed playback closes the first-recording presentation beat")
    _check("complete" in objective.text.to_lower(), "HUD confirms first recording completion")

    clip = null
    scene.queue_free()
    await process_frame
    await create_timer(0.1).timeout
    print("Presentation contract tests complete. Failures: ", failures)
    call_deferred("quit", failures)
