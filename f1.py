while True:
	for i in range(get_world_size()):
		move(North)
	move(East)
	for i in range(get_world_size()):
		move(South)
	move(East)
	x, y = get_pos_x(), get_pos_y()
	length = get_world_size()
	if x== length -1:
		for i in range(get_world_size()):
			move(West)
			
	