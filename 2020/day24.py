from collections import Counter

with open("data/small_input_for_day24.txt", "r") as f:
    text = f.readlines()

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
                easts -= 1
                nws -= 1
            else:
                nws -= 1
            line_to_edit = line_to_edit[2:]
    checklist.append((easts, nws))

black = 0
for elt in Counter(checklist):
    occurs = checklist.count(elt)
    print(elt, occurs)
    if not occurs%2:
        black += 1
print(black)