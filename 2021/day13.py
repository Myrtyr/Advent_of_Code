with open("2021/data/input_day13.txt", "r") as f:
    lines = f.read()

dots, folds = lines.split("\n\n")
dots = dots.split("\n")
folds = folds.split("\n")

# Puzzle 1
print(folds[0])
dot_list = []
for dot in dots:
    x, y = dot.split(",")
    x = int(x)
    if x > 655:
        x = x - 2*(x - 655)
    y = int(y)
    if [x,y] not in dot_list:
        dot_list.append([x,y])
print(len(dot_list))

# Puzzle 2
print(folds)
xs = [655, 327, 163, 81, 40]
ys = [447, 223, 111, 55, 27, 13, 6]

dot_list = []
for dot in dots:
    x, y = dot.split(",")

    x = int(x)
    for x_fold in xs:
        if x > x_fold:
            x = x - 2*(x - x_fold)

    y = int(y)
    for y_fold in ys:
        if y > y_fold:
            y = y - 2*(y - y_fold)

    if [x,y] not in dot_list:
        dot_list.append([x,y])

# Print code
for y_coord in range(6):
    print()
    for x_coord in range(40):
        if x_coord%5:
            print(" ", end="")
        if [x_coord, y_coord] in dot_list:
            print("#", end="")
        else:
            print(".",end="")