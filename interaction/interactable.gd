extends Area3D
class_name Interactable

@export var interaction_prompt: String = "Interact"
@export var interaction_priority: int = 0
@export var interaction_enabled: bool = true

func can_interact(_actor: Node) -> bool:
    return interaction_enabled

func get_interaction_prompt(_actor: Node) -> String:
    return interaction_prompt

func interact(_actor: Node) -> void:
    pass
