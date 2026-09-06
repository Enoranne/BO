extends Node
class_name InteractionContext

signal interactable_changed(interactable: Interactable)
signal recordable_source_changed(source: RecordableSource)

@export_node_path("Area3D") var sensor_path: NodePath
@export_node_path("Node3D") var actor_path: NodePath

var current_interactable: Interactable
var current_recordable_source: RecordableSource

@onready var sensor: Area3D = get_node_or_null(sensor_path)
@onready var actor: Node3D = get_node_or_null(actor_path)

func _physics_process(_delta: float) -> void:
    refresh()

func refresh() -> void:
    if sensor == null or actor == null:
        _set_interactable(null)
        _set_recordable_source(null)
        return

    _set_interactable(_choose_interactable(sensor.get_overlapping_areas()))
    _set_recordable_source(_choose_recordable_source(sensor.get_overlapping_areas()))

func interact_current() -> bool:
    if current_interactable == null or actor == null:
        return false
    if not current_interactable.can_interact(actor):
        return false
    current_interactable.interact(actor)
    refresh()
    return true

func get_current_prompt() -> String:
    if current_interactable == null or actor == null:
        return ""
    if not current_interactable.can_interact(actor):
        return ""
    return current_interactable.get_interaction_prompt(actor)

func _choose_interactable(areas: Array[Area3D]) -> Interactable:
    var best: Interactable
    var best_priority := -2147483648
    var best_distance := INF

    for area in areas:
        if area is not Interactable:
            continue
        var candidate := area as Interactable
        if not candidate.can_interact(actor):
            continue
        var distance := actor.global_position.distance_squared_to(candidate.global_position)
        if candidate.interaction_priority > best_priority or (candidate.interaction_priority == best_priority and distance < best_distance):
            best = candidate
            best_priority = candidate.interaction_priority
            best_distance = distance
    return best

func _choose_recordable_source(areas: Array[Area3D]) -> RecordableSource:
    var best: RecordableSource
    var best_priority := -2147483648
    var best_distance := INF

    for area in areas:
        if area is not RecordableSource:
            continue
        var candidate := area as RecordableSource
        if not candidate.can_record():
            continue
        var distance := actor.global_position.distance_squared_to(candidate.global_position)
        if candidate.recording_priority > best_priority or (candidate.recording_priority == best_priority and distance < best_distance):
            best = candidate
            best_priority = candidate.recording_priority
            best_distance = distance
    return best

func _set_interactable(value: Interactable) -> void:
    if value == current_interactable:
        return
    current_interactable = value
    interactable_changed.emit(current_interactable)

func _set_recordable_source(value: RecordableSource) -> void:
    if value == current_recordable_source:
        return
    current_recordable_source = value
    recordable_source_changed.emit(current_recordable_source)
