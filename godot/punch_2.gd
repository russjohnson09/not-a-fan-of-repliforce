extends Node2D




func _ready():
	print("start")
	
	$AnimationPlayer.play("new_animation", -1, 1.2)
	pass


func _on_animation_player_animation_finished(anim_name: StringName) -> void:
	
	pass # Replace with function body.
