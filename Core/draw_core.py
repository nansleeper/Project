#from ..map_array.map import map_array  #FIXIT
#print(map_array[1][1])

def calculate_coard(objects, player):
    
    for object_type in objects:
        for oblect in object_type:
            object.localx = object.x - player.x
            object.localy = object.y - player.y




def map_compile(player_x, player_y, map_array):

    for map_object in map_array:
        if abs(map_object.localx) - 150 <= 900 and abs(map_object.localy) - 150 <= 450:
            map_object.draw()

