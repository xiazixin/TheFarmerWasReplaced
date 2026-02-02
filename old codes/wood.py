def drone_function():
	while True:

		move(West)
	
		x, y = get_pos_x(), get_pos_y()
		length = get_world_size()
	
	#if can_harvest():
		#harvest()
		if (x + y) % 2 != 0:
			if can_harvest():
				harvest()
			plant(Entities.Tree)
			#use_item(Items.Fertilizer)
		#else:
			#plant(Entities.Bush)
	
	
		if x == length -1:
			move(North)
	do_a_flip()
spawn_drone(drone_function)

while True:

	move(North)
	
	x, y = get_pos_x(), get_pos_y()
	length = get_world_size()
	
	#if can_harvest():
		#harvest()
	if (x + y) % 2 != 0:
		if can_harvest():
			harvest()
		plant(Entities.Tree)
			#use_item(Items.Fertilizer)
		#else:
			#plant(Entities.Bush)
	
	
	if y == length -1:
		move(East)
do_a_flip()
