


straight_array = []
gamemap_size = (47, 31)
gameblock_size = 300

i = 0
with open("map_array/mapinfo.txt", "r") as gamemap:
    for line in gamemap:
        if i % 2 == 0:
            straight_array.append(line)
        i += 1



map_array_line = []
map_array = []

for y in range(gamemap_size[1]):
    for x in range(gamemap_size[0]):
        element = straight_array[x + gamemap_size[0] * y].split()
        map_array_line.append(element[2])
    map_array.append(map_array_line)
    map_array_line = []









