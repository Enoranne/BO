extends SceneTree
## Structural runtime A/B evidence only. Does not approve pixels or lighting.

var failures := 0


func _initialize() -> void:
    call_deferred("_run")


func _check(condition: bool, message: String) -> void:
    if condition:
        print("PASS: ", message)
    else:
        failures += 1
        push_error("FAIL: " + message)


func _physics_signature(node: Node, base: Node, result: Dictionary) -> void:
    var values := {}
    if node is CollisionObject3D:
        values["transform"] = (node as Node3D).transform
        values["layer"] = (node as CollisionObject3D).collision_layer
        values["mask"] = (node as CollisionObject3D).collision_mask
    if node is CollisionShape3D:
        var collider := node as CollisionShape3D
        values["transform"] = collider.transform
        values["disabled"] = collider.disabled
        values["bounds"] = collider.shape.get_debug_mesh().get_aabb()
    if node is Marker3D:
        values["transform"] = (node as Node3D).transform
    if not values.is_empty():
        result[str(base.get_path_to(node))] = values
    for child in node.get_children():
        _physics_signature(child, base, result)


func _inspect(path: String, wrapper: bool) -> Dictionary:
    var packed := load(path) as PackedScene
    _check(packed != null, "Runtime scene loads: " + path)
    if packed == null:
        return {}
    var scene := packed.instantiate()
    root.add_child(scene)
    await process_frame
    await physics_frame
    await process_frame
    var base: Node = scene.get_node("Base") if wrapper else scene
    var result := {}
    _physics_signature(base.get_node("Set"), base, result)
    _physics_signature(base.get_node("Blocking"), base, result)
    var camera := base.get_node("CinematicCamera") as Camera3D
    result["camera_position"] = camera.position
    result["camera_fov"] = camera.fov
    var wall := base.get_node("Set/BackWall/Mesh") as MeshInstance3D
    var label := base.get_node("FisherPrice/Label") as Label3D
    _check((wall.material_override != null) == wrapper, "Materials remain scoped to the wrapper")
    _check(label.visible != wrapper, "World label visibility remains scoped to the wrapper")
    var hud := base.get_node("HUD") as RecorderHUD
    _check(hud.minimal_context_hints == wrapper, "Context HUD remains scoped to the wrapper")
    if wrapper:
        _check(base.has_node("VisualSetDressing"), "Visual Slice dressing builds in the engine")
        _check(base.has_node("FisherPrice/VisualDetails/CassettePanel"), "Fisher presentation detail builds in the engine")
        var dressing := base.get_node("VisualSetDressing")
        var count := dressing.get_child_count()
        scene.get_node("Period1982SetDressing").apply_set_dressing()
        _check(dressing.get_child_count() == count, "Dressing does not duplicate when reapplied")
    scene.queue_free()
    await process_frame
    return result


func _run() -> void:
    var baseline: Dictionary = await _inspect("res://scenes/piste_0/christmas_1982/Christmas1982.tscn", false)
    var visual: Dictionary = await _inspect("res://scenes/piste_0/christmas_1982/Christmas1982_VisualSlice.tscn", true)
    _check(not baseline.is_empty() and baseline == visual, "A/B preserves collider shapes, layers, transforms, blocking and camera anchor/FOV")

    var packed := load("res://scenes/piste_0/christmas_1982/CharacterReadabilityPreview.tscn") as PackedScene
    _check(packed != null, "CharacterReadabilityPreview loads in the engine")
    if packed != null:
        var preview := packed.instantiate()
        root.add_child(preview)
        await process_frame
        var malo := preview.get_node("MaloPreview") as PlaceholderHumanoid3D
        var ronan := preview.get_node("RonanPreview") as PlaceholderHumanoid3D
        _check(malo.has_node("Head") and ronan.has_node("Head"), "Both procedural character rigs instantiate")
        _check(malo.has_node("Label") and ronan.has_node("Label"), "Preview labels coexist with character geometry")
        _check(is_equal_approx(malo.stature, 1.45) and is_equal_approx(ronan.stature, 1.68), "Authored placeholder statures are preserved; likeness is not approved")
        _check(ronan.stature > malo.stature, "Ronan remains taller than Malo")
        preview.queue_free()
        await process_frame
    print("Sprint 5 scene contract tests complete. Failures: ", failures)
    call_deferred("quit", failures)
