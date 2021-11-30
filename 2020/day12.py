import numpy as np

text = []
for line in open("data/input_for_day12.txt", "r"):
    text.append(line.rstrip())

wind = ["N", "E", "S", "W"]


def move(nose, let, num):
    if let == "R":
        new_nose = int(int(num) / 90)
        nose = (nose + new_nose)%4
        hor = 0
        ver = 0
    elif let == "L":
        new_nose = -int(int(num) / 90)
        nose = (nose + new_nose)%4
        hor = 0
        ver = 0
    elif let == "F":
        let = wind[nose]
    if let == "N":
        ver = int(num)
        hor = 0
    elif let == "E":
        ver = 0
        hor = int(num)
    elif let == "S":
        ver = -int(num)
        hor = 0
    elif let == "W":
        ver = 0
        hor = -int(num)
    return nose, np.array((hor, ver))

location = np.array((0,0))
direction = 1
for letter_number in text:
    letter = letter_number[0]
    number = letter_number[1:]
    direction, location_increase = move(direction, letter, number)
    location += location_increase
print(sum(abs(location)))

def move_waypoint(way_loc, boat_loc, move_letter, move_number):
    if move_letter == "L":
        x,y = way_loc-boat_loc
        theta = np.radians(int(move_number))
        new_way = boat_loc + np.array([round(x*np.cos(theta) - y*np.sin(theta)), round(y*np.cos(theta) + x*np.sin(theta))])
    elif move_letter == "R":
        x,y = way_loc-boat_loc
        theta = np.radians(int("-"+move_number))
        new_way = boat_loc + np.array([round(x*np.cos(theta) - y*np.sin(theta)), round(y*np.cos(theta) + x*np.sin(theta))])
    elif move_letter == "F":
        dist_boat_way = np.array(way_loc-boat_loc)
        boat_loc += int(move_number)*dist_boat_way
        new_way = boat_loc + dist_boat_way
    if move_letter == "N":
        new_way = waypoint + np.array([0, int(move_number)])
    elif move_letter == "E":
        new_way = waypoint + np.array([int(move_number), 0])
    elif move_letter == "S":
        new_way = waypoint + np.array([0, -int(move_number)])
    elif move_letter == "W":
        new_way = waypoint + np.array([-int(move_number), 0])
    return new_way, boat_loc

waypoint = np.array((10,1))
ship = np.array((0,0))
for letter_number in text:
    print(waypoint, ship)
    letter = letter_number[0]
    number = letter_number[1:]
    waypoint, ship = move_waypoint(waypoint, ship, letter, number)
print(ship)
print(abs(ship))
print(sum(abs(ship)))
