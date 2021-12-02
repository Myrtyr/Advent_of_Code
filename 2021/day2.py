with open("2021/data/input_day2.txt", "r") as f:
    directions = f.readlines()

#replace <directions> by <example> to run example
example = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]


# puzzle 1
hor = 0
dep = 0
for direction in directions:
    dir, steps = direction.split(" ")
    if dir == "forward":
        hor += int(steps)
    elif dir == "down":
        dep += int(steps)
    elif dir == "up":
        dep -= int(steps)
    else:
        print(direction)
print(hor*dep)

# puzzle 2
hor = 0
dep = 0
aim = 0
for direction in directions:
    dir, steps = direction.split(" ")
    if dir == "forward":
        hor += int(steps)
        dep += int(steps)*aim
    elif dir == "down":
        aim += int(steps)
    elif dir == "up":
        aim -= int(steps)
    else:
        print(direction)
print(hor*dep)