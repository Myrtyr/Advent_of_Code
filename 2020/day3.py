
def sloper(right, down):
    trees = 0
    with open("data/input_for_day3.txt", "r") as f:
        line = f.readline()
        col = 0
        trees += line[col] == "#"
        line = f.readline()
        while line != "":
            col += right
            col = col % 31
            tree_location = line[col]
            if tree_location == "#":
                trees += 1
            line = f.readline()
    return trees

trees = 0
with open("data/input_for_day3.txt", "r") as f:
    line = f.readline()
    col = 0
    trees += line[col] == "#"
    line = f.readline()
    line = f.readline()
    while line != "":
        col += 1
        col = col % 31
        tree_location = line[col]
        if tree_location == "#":
            trees += 1
        line = f.readline()
        line = f.readline()
stsja = trees


print(sloper(3,1)*sloper(1,1)*sloper(5,1)*sloper(7,1)*stsja)