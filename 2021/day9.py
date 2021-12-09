import numpy as np
from scipy.ndimage import measurements


with open('2021/data/input_day9.txt', 'r') as f:
    rows = f.readlines()

no_rows = len(rows)
no_cols = len(rows[0]) - 1
risk = 0
minima = {}
for row_index in range(no_rows):
    row = rows[row_index].rstrip()
    for col_index in range(no_cols):
        minim = True
        current = int(row[col_index])
        if col_index > 0:
            neighbor = int(row[col_index - 1])
            # print("left",neighbor)
            if neighbor <= current:
                minim = False
        if col_index < no_cols - 1:
            neighbor = int(row[col_index + 1])
            # print("right",neighbor)
            if neighbor <= current:
                minim = False
        if row_index > 0:
            neighbor = int(rows[row_index - 1][col_index])
            # print("bot",neighbor)
            if neighbor <= current:
                minim = False
        if row_index < no_rows - 1:
            neighbor = int(rows[row_index + 1][col_index])
            # print("top",neighbor)
            if neighbor <= current:
                minim = False
        if minim:
            risk += int(current) + 1
            minima[(row_index, col_index)] = 0
print(risk)

# Puzzle 2
watershed_matrix = np.zeros((no_rows+2, no_cols+2))
for row_index in range(no_rows):
    row = rows[row_index].rstrip()
    for col_index in range(no_cols):
        item = int(row[col_index]) != 9
        watershed_matrix[row_index + 1, col_index + 1] = item

# sorry I cheated and used scipy, I really don't like this puzzle
lw, num = measurements.label(watershed_matrix)
area = sorted(measurements.sum(watershed_matrix, lw, index=np.arange(lw.max() + 1)))
print(area[-1]*area[-2]*area[-3])