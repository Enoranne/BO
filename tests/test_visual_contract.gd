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
    _check(packed != null, "Christmas1982 loads for visual contract")
    if packed == null:
        quit(failures)
        return

    var scene := packed.instantiate()
    root.add_child(scene)
    await process_frame
    await physics_frame

    for path in [
        "Set/Floor",
        "Set/BackWall",
        "Set/LeftWall",
        "Set/RightWall",
        "Set/FrontBoundary",
        "Set/SofaPlaceholder",
        "Set/FireplacePlaceholder",
        "Set/CoffeeTablePlaceholder",
        "Set/TreePlaceholder",
        "Set/GiftPile",
        "Lighting/FireGlow",
        "Lighting/TreeLamp",
        "Malo",
        "FisherPrice",
        "RonanTest",
        "CinematicCamera"
    ]:
        _check(scene.has_node(path), "Visual contract node exists: " + path)

    var malo := scene.get_node("Malo") as Node3D
    var fisher := scene.get_node("FisherPrice") as Node3D
    var ronan := scene.get_node("RonanTest") as Node3D
    var camera := scene.get_node("CinematicCamera") as Camera3D

    _check(malo.global_position.distance_to(fisher.global_position) < 5.5,
        "Fisher Price is within a short opening walk from Malo")
    _check(fisher.global_position.distance_to(ronan.global_position) < 3.5,
        "RonanTest is close enough to establish the first recording loop")
    _check(camera.current, "Cinematic camera starts current")
    _check(camera.fov <= 50.0, "Opening camera keeps a cinematic field of view")

    print("Visual contract tests complete. Failures: ", failures)
    quit(failures)
