import numpy as np
with open("2021/data/input_day15.txt", "r") as f:
    lines = f.readlines()

size = 100
distances = np.zeros((size,size))
for index_ver in range(len(lines)):
    line = lines[index_ver].rstrip()
    for index_hor in range(len(line)):
        distance = line[index_hor]
        distances[index_ver,index_hor] = distance


def neighbours(index_ver, index_hor, len = size):
    nbrs = []
    if index_ver > 0:
        nbrs.append([index_ver-1, index_hor])
    if index_ver < len-1:
        nbrs.append([index_ver+1, index_hor])
    if index_hor > 0:
        nbrs.append([index_ver, index_hor-1])
    if index_hor < len-1:
        nbrs.append([index_ver, index_hor+1])
    return nbrs


def dijkstra(distance_matrix, start, size_here):
    path_lengths = 10000 * np.ones((size_here, size_here))
    path_lengths[start[0], start[1]] = 0
    unvisited = []
    for i in range(size_here):
        for j in range(size_here):
            unvisited.append((i,j))
    while unvisited:
        print(len(unvisited))
        current_node = unvisited[0]
        for node in unvisited:
            path_length = path_lengths[node[0],node[1]]
            if path_length < path_lengths[current_node[0],current_node[1]]:
                current_node = node
            if current_node == (size_here,size_here):
                break
        neighbs = neighbours(current_node[0], current_node[1], size_here)
        for neighb in neighbs:
            new_path = path_lengths[current_node[0], current_node[1]] + distance_matrix[neighb[0], neighb[1]]
            if new_path < path_lengths[neighb[0], neighb[1]]:
                path_lengths[neighb[0], neighb[1]] = new_path
        unvisited.remove(current_node)
    return path_lengths


# Puzzle 1
print(dijkstra(distances, [0, 0], size)[-1, -1])

# Puzzle 2
big_distances = distances.copy()
new_matrices = [big_distances]
for row in range(4):
    new_matrices.append(new_matrices[-1] % 9 + 1)
big_distances = np.concatenate(new_matrices, axis=0)
new_matrices = [big_distances]
for col in range(4):
    new_matrices.append(new_matrices[-1] % 9 + 1)
big_distances = np.concatenate(new_matrices, axis=1)

print(dijkstra(big_distances, [0, 0], size*5)[-1, -1])

