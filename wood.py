while True:
	for i in range(get_world_size()):
		move(North)
	
		x, y = get_pos_x(), get_pos_y()
		length = get_world_size()
	
		if can_harvest():
			harvest()
			if (x + y) % 2 != 0:
				plant(Entities.Tree)
				#use_item(Items.Fertilizer)
			else:
				plant(Entities.Bush)
	
	
	if y == length -1:
		move(East)
		
			
	
	if y == 0:
		move(East)

do_a_flip()