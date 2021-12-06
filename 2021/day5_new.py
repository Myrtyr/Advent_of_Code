import numpy as np

with open("2021/data/input_day5.txt", "r") as f:
    data = f.readlines()

locs = np.zeros((1000,1000))
for line in data:
    start, arrow, end = line.split()
    start_x = int(start.split(",")[0])
    start_y = int(start.split(",")[1])
    end_x = int(end.split(",")[0])
    end_y = int(end.split(",")[1])

    if start_x == end_x:
        locs[start_y:end_y+1, start_x] += 1
        locs[end_y:start_y+1, start_x] += 1

    elif start_y == end_y:
        locs[end_y, start_x:end_x+1] += 1
        locs[end_y, end_x:start_x+1] += 1

    else:
        y_index = start_y
        if end_y < start_y:
            increase = -1
        else:
            increase = 1
        if start_x <= end_x:
            for x_index in range(start_x, end_x+1):
                locs[y_index, x_index] += 1
                y_index += increase
        else:
            y_index = end_y
            increase = -increase
            for x_index in range(end_x, start_x+1):
                locs[y_index, x_index] += 1
                y_index += increase
    print(locs)

answer = np.where(locs >= 2)
print(len(answer[0]))

