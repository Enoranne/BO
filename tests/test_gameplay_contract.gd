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
    _check(packed != null, "Christmas1982 loads as a PackedScene")
    if packed == null:
        quit(failures)
        return

    var scene := packed.instantiate()
    root.add_child(scene)
    await process_frame
    await physics_frame

    var malo := scene.get_node("Malo") as MaloController
    var fisher := scene.get_node("FisherPrice") as FisherPrice
    var ronan := scene.get_node("RonanTest") as RecordableSource

    _check(malo != null, "Malo exists")
    _check(fisher != null, "Fisher Price exists")
    _check(ronan != null, "RonanTest exists")
    _check(malo.equipped_recorder == null, "Malo starts without a recorder")
    _check(not malo.try_begin_recording(), "Malo cannot REC before taking the Fisher Price")

    fisher.interact(malo)
    _check(malo.equipped_recorder != null, "Taking Fisher Price equips its Recorder")
    _check(fisher.device_state == FisherPrice.DeviceState.EQUIPPED, "Fisher Price enters EQUIPPED state")

    malo.nearby_source = ronan
    _check(malo.try_begin_recording(), "Malo can REC RonanTest after equipping Fisher Price")
    _check(fisher.device_state == FisherPrice.DeviceState.ACTIVE, "Fisher Price enters ACTIVE state during REC")
    _check(not malo.try_begin_recording(), "Malo cannot start two recordings simultaneously")

    await create_timer(0.15).timeout
    var clip := malo.try_stop_recording()
    _check(clip != null, "STOP creates the first clip")
    _check(fisher.device_state == FisherPrice.DeviceState.EQUIPPED, "Fisher Price returns to EQUIPPED after STOP")
    _check(malo.equipped_recorder.clips.size() == 1, "Exactly one clip exists after first STOP")

    _check(malo.try_play_latest(), "Malo can PLAY the latest clip")
    _check(fisher.device_state == FisherPrice.DeviceState.ACTIVE, "Fisher Price enters ACTIVE state during PLAY")
    malo.equipped_recorder.stop()
    _check(malo.equipped_recorder.state == Recorder.State.STOP, "Loop ends in STOP")

    clip = null
    scene.queue_free()
    await process_frame
    await create_timer(0.1).timeout
    print("Gameplay contract tests complete. Failures: ", failures)
    call_deferred("quit", failures)
