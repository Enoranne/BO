extends Area3D
class_name RecordableSource

@export var source_id: StringName = &"source"
@export var clip_title: String = "Untitled"
@export var audio_stream: AudioStream
@export var recording_priority: int = 0
@export var recordable_enabled: bool = true
@export var source_metadata: Dictionary = {}

@onready var preview_player: AudioStreamPlayer3D = get_node_or_null("PreviewPlayer")

func can_record() -> bool:
    return recordable_enabled and audio_stream != null

func get_recording_stream() -> AudioStream:
    return audio_stream if can_record() else null

func get_recording_metadata() -> Dictionary:
    var metadata := source_metadata.duplicate(true)
    metadata["source_id"] = String(source_id)
    metadata["source_title"] = clip_title
    return metadata

func preview() -> bool:
    if preview_player == null or not can_record():
        return false
    preview_player.stream = audio_stream
    preview_player.play()
    return true
