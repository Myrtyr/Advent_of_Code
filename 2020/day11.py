with open("data/input_for_day11.txt", "r") as f:
    text = f.readlines()

seats = []
for elt in text:
    seats.append(list(elt.rstrip()))


def surrounding(seatset, rows, cols):
    surrounding_seats = []
    width = len(seatset) - 1
    height = len(seatset[0]) - 1
    if rows > 0:
        surrounding_seats.append(seatset[rows - 1][cols])
        if cols > 0:
            surrounding_seats.append(seatset[rows - 1][cols - 1])
        if cols < height:
            surrounding_seats.append(seatset[rows - 1][cols + 1])
    if rows < width:
        surrounding_seats.append(seatset[rows + 1][cols])
        if cols > 0:
            surrounding_seats.append(seatset[rows + 1][cols - 1])
        if cols < height:
            surrounding_seats.append(seatset[rows + 1][cols + 1])
    if cols > 0:
        surrounding_seats.append(seatset[rows][cols - 1])
    if cols < height:
        surrounding_seats.append(seatset[rows][cols + 1])
    return surrounding_seats


def rules(seatset, rows, cols):
    seat = seatset[rows][cols]
    if seat == "L" and surrounding(seatset, rows, cols).count("#") == 0:
        resseat = "#"
    elif seat == "#" and surrounding(seatset, rows, cols).count("#") >= 4:
        resseat = "L"
    else:
        resseat = seat
    return resseat


oldseats = seats.copy()
for i in range(100):
    newseats = []
    for row in range(len(oldseats)):
        newseats.append([])
        for col in range(len(oldseats[0])):
            newseats[row].append(rules(oldseats, row, col))
    if newseats == oldseats:
        print(sum([row_of_seats.count("#") for row_of_seats in newseats]))
        break
    else:
        oldseats = newseats.copy()


def line_of_sight(seatset, rows, cols):
    surrounding_seats = []
    height = len(seatset)
    south = height - rows - 1
    north = rows
    width = len(seatset[0])
    east = width - cols - 1
    west = cols
    northeast = min(north, east)
    northwest = min(north, west)
    southeast = min(south, east)
    southwest = min(south, west)
    #print(rows, cols, north, northeast, east, southeast, south, southwest, west, northwest)
    for increment in range(1, north + 1):
        if seatset[rows - increment][cols] != ".":
            surrounding_seats.append(seatset[rows - increment][cols])
            break
    for increment in range(1, south + 1):
        if seatset[rows + increment][cols] != ".":
            surrounding_seats.append(seatset[rows + increment][cols])
            break
    for increment in range(1, east + 1):
        if seatset[rows][cols + increment] != ".":
            surrounding_seats.append(seatset[rows][cols + increment])
            break
    for increment in range(1, west + 1):
        if seatset[rows][cols - increment] != ".":
            surrounding_seats.append(seatset[rows][cols - increment])
            break
    for increment in range(1, northeast + 1):
        if seatset[rows - increment][cols + increment] != ".":
            surrounding_seats.append(seatset[rows - increment][cols + increment])
            break
    for increment in range(1, northwest + 1):
        if seatset[rows - increment][cols - increment] != ".":
            surrounding_seats.append(seatset[rows - increment][cols - increment])
            break
    for increment in range(1, southeast + 1):
        if seatset[rows + increment][cols + increment] != ".":
            surrounding_seats.append(seatset[rows + increment][cols + increment])
            break
    for increment in range(1, southwest + 1):
        if seatset[rows + increment][cols - increment] != ".":
            surrounding_seats.append(seatset[rows + increment][cols - increment])
            break
    return surrounding_seats


def rules2(seatset, rows, cols):
    seat = seatset[rows][cols]
    if seat == "L" and line_of_sight(seatset, rows, cols).count("#") == 0:
        resseat = "#"
    elif seat == "#" and line_of_sight(seatset, rows, cols).count("#") >= 5:
        resseat = "L"
    else:
        resseat = seat
    return resseat


oldseats = seats.copy()
for i in range(100):
    newseats = []
    for row in range(len(oldseats)):
        newseats.append([])
        for col in range(len(oldseats[0])):
            newseat = rules2(oldseats, row, col)
            newseats[row].append(newseat)
    if newseats == oldseats:
        print(sum([row_of_seats.count("#") for row_of_seats in newseats]))
        break
    else:
        oldseats = newseats.copy()
