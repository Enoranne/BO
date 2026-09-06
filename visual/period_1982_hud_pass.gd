extends Node
class_name Period1982HUDPass

## Visual-only HUD treatment for the Sprint 5 Christmas1982 wrapper.
## It may change wording emphasis and Control presentation, but never gameplay state.

@export var root_path: NodePath = NodePath("..")
@export var apply_on_ready := true

const OBJECTIVE_PREFIX := "OBJECTIVE  "
const WARM_CREAM := Color(0.90, 0.82, 0.67, 0.90)
const WARM_SOFT := Color(0.82, 0.74, 0.62, 0.76)
const WARM_MUTED := Color(0.72, 0.65, 0.55, 0.58)
const WARM_HINT := Color(0.93, 0.86, 0.73, 0.88)

func _ready() -> void:
    if apply_on_ready:
        call_deferred("apply_hud_pass")

func apply_hud_pass() -> void:
    var root := get_node_or_null(root_path)
    if root == null:
        push_warning("Period1982HUDPass: root_path does not resolve: %s" % root_path)
        return

    var hud := root.get_node_or_null("HUD")
    if hud == null:
        return

    # Configure the existing presentation-only HUD without changing its gameplay signal sources.
    hud.set("objective_prefix", "")
    hud.set("compact_hints", true)
    hud.set("teach_legacy_play_key", false)

    var objective := root.get_node_or_null("HUD/Margin/VBox/Objective") as Label
    var state := root.get_node_or_null("HUD/Margin/VBox/State") as Label
    var timer := root.get_node_or_null("HUD/Margin/VBox/Timer") as Label
    var source := root.get_node_or_null("HUD/Margin/VBox/Source") as Label
    var hint := root.get_node_or_null("HUD/Margin/VBox/Hint") as Label
    var vbox := root.get_node_or_null("HUD/Margin/VBox") as VBoxContainer

    if objective != null:
        if objective.text.begins_with(OBJECTIVE_PREFIX):
            objective.text = objective.text.substr(OBJECTIVE_PREFIX.length())
        _style_label(objective, 15, WARM_SOFT)
    if state != null:
        _style_label(state, 24, WARM_CREAM)
    if timer != null:
        _style_label(timer, 16, WARM_SOFT)
    if source != null:
        _style_label(source, 13, WARM_MUTED)
    if hint != null:
        _style_label(hint, 16, WARM_HINT)
    if vbox != null:
        vbox.add_theme_constant_override("separation", 4)

func _style_label(label: Label, size: int, color: Color) -> void:
    label.add_theme_font_size_override("font_size", size)
    label.add_theme_color_override("font_color", color)
