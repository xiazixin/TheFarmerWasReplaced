while True:
	move(North)
	x, y = get_pos_x(), get_pos_y()
	length = get_world_size()
	
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	

	plant(Entities.Cactus)
	swap(North)
	
	
	if y == length -1:
		move(East)


do_a_flip()