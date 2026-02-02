clear()

def check_pumpkin():
	if get_pos_x() != 0:
		move(East)
	
	left_id = measure()
	move(West)
	right_id = measure()
	move(East)
	
	return left_id == right_id


def harvest_column():
	while True: 
		if get_pos_y() != 0:
			move_to(get_pos_x(), 0) 
			
		for _ in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
				
			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)

				
			if get_water() < 0.75:
				use_item(Items.Water)
			
			
			if get_entity_type() == None:
				plant(Entities.Pumpkin)
				
			
			
		
			move(North)
		
def main_loop():
	world_size = get_world_size()

	for i in range(world_size - 1):
		if spawn_drone(harvest_column):
			move(East)
	harvest_column()
	
	
while True:
	main_loop()
	first_pass = False
	
	if check_pumpkin():
		harvest() 
		first_pass = True
		move(West)
		