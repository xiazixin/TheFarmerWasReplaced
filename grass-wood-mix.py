while True:
	move(North)
	x, y = get_pos_x(), get_pos_y()
	length = get_world_size()
	
	if can_harvest():
			harvest()
			if (x + y) % 2 != 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Grass)
	
	
	if y == length -1:
		move(East)


do_a_flip()