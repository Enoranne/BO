extends Resource
class_name RecordingClip

@export var clip_name: String = "Untitled recording"
@export var source_id: StringName = &"unknown"
@export var source_title: String = "Unknown source"
@export var duration_seconds: float = 0.0
@export var created_unix_time: int = 0
@export var metadata: Dictionary = {}
@export var stream: AudioStream

func is_playable() -> bool:
    return stream != null and duration_seconds > 0.0
