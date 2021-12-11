import numpy as np

with open("2021/data/input_day11.txt", "r") as f:
    lines = f.readlines()

octos = np.zeros((10,10))
for x_index in range(10):
    for y_index in range(10):
        octos[x_index, y_index] = lines[x_index][y_index]


def single_step(octo_matrix):
    octo_matrix += 1
    al_geweest = []
    news = True
    while news:
        new_matrix = octo_matrix
        nines_x, nines_y = np.where(octo_matrix > 9)
        news = False
        for index in range(len(nines_x)):
            nine_x = nines_x[index]
            nine_y = nines_y[index]
            if not ((nine_x, nine_y) in al_geweest):
                al_geweest.append((nine_x, nine_y))
                news = True
                if nine_x > 0:
                    new_matrix[nine_x - 1, nine_y] += 1
                    if nine_y > 0:
                        new_matrix[nine_x - 1, nine_y - 1] += 1
                    if nine_y < 9:
                        new_matrix[nine_x - 1, nine_y + 1] += 1
                if nine_x < 9:
                    new_matrix[nine_x + 1, nine_y] += 1
                    if nine_y > 0:
                        new_matrix[nine_x + 1, nine_y - 1] += 1
                    if nine_y < 9:
                        new_matrix[nine_x + 1, nine_y + 1] += 1
                if nine_y > 0:
                    new_matrix[nine_x, nine_y-1] += 1
                if nine_y < 9:
                    new_matrix[nine_x, nine_y+1] += 1
    for coord in al_geweest:
        octo_matrix[coord[0], coord[1]] = 0
    return octo_matrix, len(al_geweest)

# flashes = 0
# for i in range(100):
#     octos, al = single_step(octos)
#     flashes += al
# print(flashes)

step = 0
while sum(sum(octos)) != 0:
    step += 1
    octos, al = single_step(octos)
print(step)