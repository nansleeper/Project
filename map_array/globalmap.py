import pygame

#townmap - 1440 * 990
colormap = []
main_map = pygame.display.set_mode((1800, 1000))
town_map = pygame.image.load('map_array/map.bmp')
main_map.blit(town_map, ((1800 - 1440) / 2, 5))

for y in range(33):
    straight = []
    for x in range(48):
        block_color = town_map.get_at(((x + 1) * 15, (y + 1) * 15))
        if block_color == (0, 0, 0, 255):
            map_block = "House1"
        elif block_color == (0, 100, 0, 255):
            map_block = "House2"
        elif block_color == (100, 0, 0, 255):
            map_block = "House3"
        elif block_color == (230, 200, 200, 255):
            map_block = "Walk_road"
        elif block_color == (163, 73, 164, 255):
            map_block = "CrossRoad"
        elif block_color == (200, 191, 231, 255):
            map_block = "HorRoad"
        elif block_color == (195, 195, 195, 255):
            map_block = "VertRoad"
        elif block_color == (112, 146, 190, 255):
            map_block = "VertRoadUnable"
        elif block_color == (255, 174, 201, 255):
            map_block = "HorRoadUnable"
        elif block_color == (237, 28, 36, 255):
            map_block = "DownBoarder"
        elif block_color == (255, 201, 14, 255):
            map_block = "LeftBoarder"
        elif block_color == (255, 127, 39, 255):
            map_block = "UpperBoarder"
        elif block_color == (244, 96, 145, 255):
            map_block = "RightBoarder"
        elif block_color == (34, 177, 76, 255):
            map_block = "Park"
        elif block_color == (255, 242, 0, 255):
            map_block = "Beach"
        elif block_color == (0, 162, 232, 255):
            map_block = "Water"
        elif block_color == (185, 122, 87, 255):
            map_block = "Sand"
        straight.append(map_block)
    main_map.append(straight)
        
        
         


















