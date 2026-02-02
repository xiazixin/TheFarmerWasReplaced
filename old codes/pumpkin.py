while True:
	move(North)
	x, y = get_pos_x(), get_pos_y()
	length = get_world_size()
	
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)

	plant(Entities.Pumpkin)
	
	
	if y == length -1:
		move(East)


do_a_flip()