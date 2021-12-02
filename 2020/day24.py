with open("2020/data/input_for_day24.txt", "r") as f:
    text = f.readlines()


# Puzzle 1
from collections import Counter


checklist = []
for line in text:
    easts = 0
    nws = 0
    line_to_edit = line.rstrip()
    while line_to_edit != "":
        letter = line_to_edit[0]
        if letter == "e":
            easts += 1
            line_to_edit = line_to_edit[1:]
        elif letter == "w":
            easts -= 1
            line_to_edit = line_to_edit[1:]
        elif letter == "n":
            if line_to_edit[1] == "e":
                easts += 1
                nws += 1
            else:
                nws += 1
            line_to_edit = line_to_edit[2:]
        elif letter == "s":
            if line_to_edit[1] == "e":
                nws -= 1
            else:
                nws -= 1
                easts -= 1
            line_to_edit = line_to_edit[2:]
    checklist.append((easts, nws))

black = 0
counted_tiles = Counter(checklist)
for elt in counted_tiles:
    occurs = counted_tiles[elt]
    if occurs%2:
        black += 1
print(black)

# Puzzle 2
for i in range(100):
    appenddict = {}
    for elt in counted_tiles:
        e, nw = elt
        neighbours = [(e,nw+1),(e+1,nw+1), (e+1,nw), (e,nw-1), (e-1,nw-1),(e-1,nw)]
        for neighbour in neighbours:
            appenddict[neighbour] = 0
    appenddict.update(counted_tiles)
    new_count = appenddict.copy()

    for elt in appenddict:
        e, nw = elt
        neighbours = [(e,nw+1),(e+1,nw+1), (e+1,nw), (e,nw-1), (e-1,nw-1),(e-1,nw)]
        counter = 0
        for neighbour in neighbours:
            if neighbour in appenddict:
                counter += appenddict[neighbour]%2
        # counting surrounding black is done, now change tiles
        if (counter == 0 or counter > 2) and (appenddict[elt] % 2):
            new_count[elt] += 1
        elif counter == 2 and (not appenddict[elt]%2):
            new_count[elt] = 1
    counted_tiles = new_count.copy()


black = 0
for elt in new_count:
    occurs = new_count[elt]
    if occurs%2:
        black += 1
print(black)