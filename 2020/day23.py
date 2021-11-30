import numpy as np

ordering = []
with open("data/input_for_day23.txt", "r") as f:
    text = f.read()
for line in text:
    ordering.append(int(line))

current_index = 0
current_cup = ordering[current_index]
length_circle = len(ordering)

for step in range(100):
    diff = 0
    # pick up
    picked_up = []
    pickup_index = current_index + 1
    for i in range(3):
        if current_index >= length_circle - i - 1:
            diff -= 1
            pickup_index = 0
        picked_up.append(ordering.pop(pickup_index))
    # destination
    counter = 1
    while counter <= 4:
        goal = current_cup - counter
        if goal < 1:
            destination_index = np.argmax(ordering)
            break
        for i, val in enumerate(ordering):
            if val == goal:
                destination_index = i
                counter = 5
                break
        counter += 1
    # place back
    # -4 because circle is 3 smaller than start, and indices start from 0 so -1
    if destination_index == length_circle - 4:
        for i in range(3):
            ordering.append(picked_up[i])
    else:
        for i in range(3):
            ordering.insert(destination_index + 1, picked_up[3-i-1])
    # new current cup
    if destination_index < current_index:
        # because the three taken out are placed in front of it
        current_index = current_index + 3
    current_index += diff
    current_index = (current_index + 1) % length_circle
    current_cup = ordering[current_index]
print(ordering)



##############################################33
miljoen = 1000000
tienmiljoen = 10000000
new_input = np.arange(1,miljoen+1)
for i in range(len(text)):
    new_input[i] = int(text[i])
new_input = list(new_input)

current_index = 0
current_cup = new_input[current_index]
length_circle = miljoen

for step in range(tienmiljoen):
    if not step%100000:
        print(step*100//tienmiljoen,"%")
    diff = 0
    # pick up
    picked_up = []
    pickup_index = current_index + 1
    for i in range(3):
        if current_index >= length_circle - i - 1:
            diff -= 1
            pickup_index = 0
        picked_up.append(new_input.pop(pickup_index))
    # destination
    counter = 1
    while counter <= 4:
        goal = current_cup - counter
        if goal < 1:
            destination_index = np.argmax(new_input)
            break

        for i, val in enumerate(ordering):
            if val == goal:
                destination_index = i
                counter = 5
                break
        counter += 1
    # place back
    # -4 because circle is 3 smaller than start, and indices start from 0 so -1
    if destination_index == length_circle - 4:
        for i in range(3):
            new_input.append(picked_up[i])
    else:
        for i in range(3):
            new_input.insert(destination_index + 1, picked_up[3-i-1])
    # new current cup
    if destination_index < current_index:
        # because the three taken out are placed in front of it
        current_index = current_index + 3
    current_index += diff
    current_index = (current_index + 1) % length_circle
    current_cup = new_input[current_index]


index_of_one = new_input.index(1)
print(new_input[(index_of_one+1)%miljoen]*new_input[(index_of_one+2)%miljoen])

# 16577 is too low
# 2143256368 is too high
