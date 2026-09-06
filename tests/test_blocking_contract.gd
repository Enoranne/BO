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
    _check(packed != null, "Christmas1982 loads for blocking contract")
    if packed == null:
        quit(failures)
        return

    var scene := packed.instantiate()
    root.add_child(scene)
    await process_frame
    await physics_frame

    for path in [
        "Blocking/MaloStart",
        "Blocking/FisherPickupBeat",
        "Blocking/RonanRecordBeat",
        "Blocking/RonanStand",
        "Blocking/CameraStart",
        "Malo/VisualRig",
        "RonanTest/VisualRig"
    ]:
        _check(scene.has_node(path), "Blocking contract node exists: " + path)

    var malo := scene.get_node("Malo") as Node3D
    var malo_start := scene.get_node("Blocking/MaloStart") as Marker3D
    var fisher := scene.get_node("FisherPrice") as Node3D
    var fisher_beat := scene.get_node("Blocking/FisherPickupBeat") as Marker3D
    var ronan := scene.get_node("RonanTest") as Node3D
    var ronan_stand := scene.get_node("Blocking/RonanStand") as Marker3D
    var record_beat := scene.get_node("Blocking/RonanRecordBeat") as Marker3D
    var camera := scene.get_node("CinematicCamera") as Camera3D
    var camera_start := scene.get_node("Blocking/CameraStart") as Marker3D

    _check(Vector2(malo.global_position.x, malo.global_position.z).distance_to(Vector2(malo_start.global_position.x, malo_start.global_position.z)) < 0.05,
        "Malo spawn matches blocking marker")
    _check(Vector2(fisher.global_position.x, fisher.global_position.z).distance_to(Vector2(fisher_beat.global_position.x, fisher_beat.global_position.z)) < 0.05,
        "Fisher Price matches pickup blocking marker")
    _check(Vector2(ronan.global_position.x, ronan.global_position.z).distance_to(Vector2(ronan_stand.global_position.x, ronan_stand.global_position.z)) < 0.05,
        "Ronan matches blocking marker")
    _check(record_beat.global_position.distance_to(ronan.global_position) < 1.55,
        "RonanRecordBeat sits inside Malo interaction sensor range")
    _check(camera.global_position.distance_to(camera_start.global_position) < 0.05,
        "Camera starts at blocking anchor")

    var malo_rig := scene.get_node("Malo/VisualRig") as PlaceholderHumanoid3D
    var ronan_rig := scene.get_node("RonanTest/VisualRig") as PlaceholderHumanoid3D
    _check(malo_rig.get_node_or_null("Head") != null, "Malo procedural silhouette builds a head")
    _check(malo_rig.get_node_or_null("LeftArm") != null, "Malo procedural silhouette builds limbs")
    _check(ronan_rig.stature > malo_rig.stature, "Ronan placeholder is visibly taller than Malo")

    print("Blocking contract tests complete. Failures: ", failures)
    quit(failures)
