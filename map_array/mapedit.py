with open("mapinfo.txt", 'w') as map:
    for k in range(31):
        for i in range(47):
            if k % 5 != 0 and i % 5 != 0:
                print(k, i, " Building\n", file=map)
                # map.write(k, " ", i, " Building\n")
            else:
                print(k, i, " Road\n", file=map)