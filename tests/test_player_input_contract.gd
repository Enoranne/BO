extends SceneTree
## Synthetic physical-key/mouse events through Godot's input pipeline.
## This is engine integration coverage, not a manual keyboard or visual review.

var failures := 0
var _azerty := false


func _initialize() -> void:
    call_deferred("_run")


func _check(condition: bool, message: String) -> void:
    if condition:
        print("PASS: ", message)
    else:
        failures += 1
        push_error("FAIL: " + message)


func _key(physical: Key, pressed: bool) -> void:
    var event := InputEventKey.new()
    event.physical_keycode = physical
    event.keycode = physical
    if _azerty and physical == KEY_W:
        event.keycode = KEY_Z
    elif _azerty and physical == KEY_A:
        event.keycode = KEY_Q
    event.pressed = pressed
    Input.parse_input_event(event)


func _logical_key(logical: Key, physical: Key, pressed: bool) -> void:
    var event := InputEventKey.new()
    event.keycode = logical
    event.physical_keycode = physical
    event.pressed = pressed
    Input.parse_input_event(event)


func _click(pressed: bool) -> void:
    var event := InputEventMouseButton.new()
    event.button_index = MOUSE_BUTTON_LEFT
    event.pressed = pressed
    event.position = Vector2(1000, 600)
    event.global_position = event.position
    Input.parse_input_event(event)


func _frames(count: int) -> void:
    for i in range(count):
        await physics_frame


func _tap(physical: Key) -> void:
    _key(physical, true)
    await _frames(2)
    _key(physical, false)
    await _frames(2)


func _walk_axis(malo: MaloController, axis: int, destination: float, key: Key) -> void:
    var direction := signf(destination - malo.position[axis])
    _key(key, true)
    var reached := false
    for i in range(180):
        await physics_frame
        if (malo.position[axis] - destination) * direction >= 0.0:
            reached = true
            break
    _key(key, false)
    await _frames(18)
    _check(reached, "Walking through real collisions reaches the route waypoint")


func _wait_for_stop(recorder: Recorder) -> void:
    for i in range(90):
        if recorder.state == Recorder.State.STOP:
            break
        await physics_frame
    _check(recorder.state == Recorder.State.STOP, "Playback naturally returns to STOP")


func _run_case(scene_path: String, mouse_pickup: bool) -> void:
    var packed := load(scene_path) as PackedScene
    _check(packed != null, "Input route scene loads: " + scene_path)
    if packed == null:
        return
    var scene := packed.instantiate()
    root.add_child(scene)
    await _frames(6)
    var base := scene.get_node_or_null("Base")
    if base == null:
        base = scene
    var malo := base.get_node("Malo") as MaloController
    var fisher := base.get_node("FisherPrice") as FisherPrice
    var recorder := fisher.recorder
    var ronan := base.get_node("RonanTest") as RecordableSource
    var director := base.get_node("Christmas1982Director") as Christmas1982Director
    var held := base.get_node("Malo/HeldRecorderVisual") as FisherPriceVisual
    var state_label := base.get_node("HUD/Margin/VBox/State") as Label
    _check(director.beat == Christmas1982Director.Beat.FIND_FISHER, "Input route starts at FIND_FISHER")

    await _tap(KEY_R)
    await _tap(KEY_E)
    _check(malo.equipped_recorder == null and recorder.clips.is_empty(), "REC and distant E cannot bypass Fisher pickup")
    _check(recorder.state == Recorder.State.STOP, "REC-before-pickup stays in STOP")

    # Verify all four directions through physical events, with Q/Z logical
    # labels in the AZERTY cases. Never teleport or force a nearby source.
    for physical in [KEY_W, KEY_S, KEY_A, KEY_D]:
        var before := malo.position
        _key(physical, true)
        await _frames(10)
        _key(physical, false)
        await _frames(16)
        var movement := malo.position - before
        var expected := Vector3.ZERO
        match physical:
            KEY_W: expected = Vector3.FORWARD
            KEY_S: expected = Vector3.BACK
            KEY_A: expected = Vector3.LEFT
            KEY_D: expected = Vector3.RIGHT
        _check(movement.dot(expected) > 0.05, "Physical movement key works: %s (AZERTY=%s)" % [physical, _azerty])

    # Manual macOS AZERTY validation found that players may also press the literal
    # W/A letters. Verify those logical fallbacks while preserving Z/Q physical keys.
    if _azerty:
        var before_w := malo.position
        _logical_key(KEY_W, KEY_Z, true)
        await _frames(10)
        _logical_key(KEY_W, KEY_Z, false)
        await _frames(16)
        _check((malo.position - before_w).dot(Vector3.FORWARD) > 0.05,
            "Literal W fallback works on AZERTY")

        var before_a := malo.position
        _logical_key(KEY_A, KEY_Q, true)
        await _frames(10)
        _logical_key(KEY_A, KEY_Q, false)
        await _frames(16)
        _check((malo.position - before_a).dot(Vector3.LEFT) > 0.05,
            "Literal A fallback works on AZERTY")

    await _walk_axis(malo, 0, 2.45, KEY_D)
    await _walk_axis(malo, 2, 0.35, KEY_W)
    _check(malo.interaction_context.current_interactable == fisher, "Proximity selects Fisher after walking around the table")
    if mouse_pickup:
        _click(true)
        await _frames(2)
        _click(false)
        await _frames(2)
    else:
        await _tap(KEY_E)
    _check(malo.equipped_recorder == recorder, "Context pickup works via " + ("left click" if mouse_pickup else "E"))
    _check(held.visible and not fisher.visible, "Pickup swaps world and carried Fisher visuals")
    _check(director.beat == Christmas1982Director.Beat.RECORD_RONAN, "Pickup advances to RECORD_RONAN")
    _check(malo.nearby_source == ronan, "Actual sensor overlaps select Ronan")

    _key(KEY_R, true)
    await _frames(18)
    _check(recorder.state == Recorder.State.REC, "Holding R starts and sustains REC")
    _check(held.is_rec_light_visible() and "REC" in state_label.text, "REC lamp and HUD follow the Recorder")
    await _tap(KEY_SPACE)
    _check(recorder.state == Recorder.State.REC and recorder.clips.is_empty(), "Space cannot interrupt an active REC")
    _key(KEY_R, false)
    await _frames(3)
    _check(recorder.state == Recorder.State.STOP and recorder.clips.size() == 1, "Releasing R creates exactly one clip and stops REC")
    _check(not held.is_rec_light_visible(), "Releasing R switches the REC lamp off")
    _check(director.beat == Christmas1982Director.Beat.PLAY_RECORDING, "STOP advances to PLAY_RECORDING")
    if recorder.clips.is_empty():
        scene.queue_free()
        await _frames(12)
        return
    _check(recorder.clips[0].source_id == &"ronan_test", "Clip comes from the physically selected Ronan source")
    await _tap(KEY_SPACE)
    _check(recorder.state == Recorder.State.PLAY and "PLAY" in state_label.text, "Space starts PLAY and updates the HUD")
    await _wait_for_stop(recorder)
    _check(director.beat == Christmas1982Director.Beat.COMPLETE, "Natural playback completes the required beat order")
    await _tap(KEY_P)
    _check(recorder.state == Recorder.State.PLAY, "Legacy P still starts PLAY")
    await _wait_for_stop(recorder)

    # Push against the front boundary with the real controller.
    _key(KEY_S, true)
    await _frames(100)
    _key(KEY_S, false)
    await _frames(18)
    _check(malo.position.z < 3.6, "Front wall collision keeps Malo inside the salon")
    scene.queue_free()
    await _frames(12)


func _run() -> void:
    root.size = Vector2i(1280, 720)
    Input.use_accumulated_input = false
    for scene_path in [
        "res://scenes/piste_0/christmas_1982/Christmas1982.tscn",
        "res://scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn"
    ]:
        _azerty = false
        await _run_case(scene_path, false)
        _azerty = true
        await _run_case(scene_path, true)
    print("Player input contract tests complete. Failures: ", failures)
    call_deferred("quit", failures)
