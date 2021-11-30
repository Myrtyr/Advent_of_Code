with open("data/input_for_day17.txt", "r") as f:
    text = f.readlines()

grid = []
for elt in text:
    grid.append(list(elt.rstrip()))
grid = [grid]
print(grid)

def neighborhood(grid_alt, location):
    # location should be a (z,y,x) tuple
    # grid should be entire grid
    active_neighbors = 0
    inactive_neighbors = 0
    zindex, yindex, xindex = location
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                new_z = zindex + i
                new_y = yindex + j
                new_x = xindex + k
                # print(new_z >= len(grid), new_y >= len(grid[zindex]), new_x >= len(grid[zindex][yindex]))
                if new_z < 0 or new_y < 0 or new_x < 0:
                    pass
                elif new_z >= len(grid_alt) or new_y >= len(grid_alt[zindex]) or new_x >= len(grid_alt[zindex][yindex]):
                    pass
                elif grid_alt[new_z][new_y][new_x] == "#":
                    active_neighbors += 1
                else:
                    inactive_neighbors += 1
    return active_neighbors, inactive_neighbors

def rules(grid_alt, loc):
    loc_z, loc_y, loc_x = loc
    act, inact = neighborhood(grid_alt, loc)
    current = grid_alt[loc_z][loc_y][loc_x]
    if current == "#" and (act == 3 or act == 4):
        new = "#"
    elif current == "." and act == 3:
        new = "#"
    else:
        new = "."
    return new


for cycle in range(6):
    # add extra layer to sides
    want_z, want_y, want_x = len(grid)+2, len(grid[0])+2, len(grid[0][0])+2
    for zlayer in grid:
        for ylayer in zlayer:
            ylayer.append(".")
            ylayer.insert(0, ".")
        zlayer.append(["."] * want_x)
        zlayer.insert(0, ["."] * want_x)
    grid.insert(0,[["."] * want_x] * want_y)
    grid.append([["."] * want_x] * want_y)
    newgrid = []
    for z_index in range(len(grid)):
        z_layer = grid[z_index]
        newgrid.append([])
        print("z=", z_index)
        for y_index in range(len(z_layer)):
            newgrid[z_index].append([])
            y_layer = z_layer[y_index]
            print(y_layer)
            for x_index in range(len(y_layer)):
                newgrid[z_index][y_index].append(rules(grid, (z_index, y_index, x_index)))
    grid = newgrid.copy()
    print("newgrid")
    for layer in newgrid:
        print("layer")
        for line in layer:
            print(line)
    print("end of cycle", cycle)

som = 0
for layer in newgrid:
    for row in layer:
        som += row.count("#")
print(som)


# exercise 2
grid2 = []
for elt in text:
    grid2.append(list(elt.rstrip()))
grid2 = [[grid2]]


def neighborhood2(grid_alt, location):
    # location should be a (w,z,y,x) tuple
    # grid should be entire grid
    active_neighbors = 0
    inactive_neighbors = 0
    windex, zindex, yindex, xindex = location
    for h in range(-1,2):
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    new_w = windex + h
                    new_z = zindex + i
                    new_y = yindex + j
                    new_x = xindex + k
                    if new_z < 0 or new_z < 0 or new_y < 0 or new_x < 0:
                        pass
                    elif new_w >= len(grid_alt) or new_z >= len(grid_alt[windex]) or new_y >= len(grid_alt[windex][zindex]) or new_x >= len(grid_alt[windex][zindex][yindex]):
                        pass
                    elif grid_alt[new_w][new_z][new_y][new_x] == "#":
                        active_neighbors += 1
                    else:
                        inactive_neighbors += 1
    return active_neighbors, inactive_neighbors

def rules2(grid_alt, loc):
    loc_w, loc_z, loc_y, loc_x = loc
    act, inact = neighborhood2(grid_alt, loc)
    current = grid_alt[loc_w][loc_z][loc_y][loc_x]
    if current == "#" and (act == 3 or act == 4):
        new = "#"
    elif current == "." and act == 3:
        new = "#"
    else:
        new = "."
    return new


for cycle in range(6):
    # add extra layer to sides
    want_w, want_z, want_y, want_x = len(grid2)+2, len(grid2[0])+2, len(grid2[0][0])+2, len(grid2[0][0][0]) + 2
    for wlayer in grid2:
        for zlayer in wlayer:
            for ylayer in zlayer:
                ylayer.append(".")
                ylayer.insert(0, ".")
            zlayer.append(["."] * want_x)
            zlayer.insert(0, ["."] * want_x)
        wlayer.insert(0,[["."] * want_x] * want_y)
        wlayer.append([["."] * want_x] * want_y)
    grid2.insert(0, [[["."] * want_x] * want_y]*want_z)
    grid2.append([[["."] * want_x] * want_y]*want_z)
    newgrid = []
    for w_index in range(len(grid2)):
        w_layer = grid2[w_index]
        newgrid.append([])
        for z_index in range(len(w_layer)):
            z_layer = w_layer[z_index]
            newgrid[w_index].append([])
            for y_index in range(len(z_layer)):
                newgrid[w_index][z_index].append([])
                y_layer = z_layer[y_index]
                for x_index in range(len(y_layer)):
                    newgrid[w_index][z_index][y_index].append(rules2(grid2, (w_index, z_index, y_index, x_index)))
    grid2 = newgrid.copy()
    print("end of cycle", cycle)

som = 0
for anotherlayer in newgrid:
    for layer in anotherlayer:
        for row in layer:
            som += row.count("#")
print(som)
