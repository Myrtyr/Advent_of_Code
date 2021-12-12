import itertools



with open("2021/data/input_day12.txt", "r") as f:
    lines = f.readlines()

graph_dict = {}
for line in lines:
    left, right = line.rstrip().split("-")
    if left not in graph_dict:
        graph_dict[left] = []
    if right not in graph_dict:
        graph_dict[right] = []
    graph_dict[left].append(right)
    graph_dict[right].append(left)


def DFS(u, v, visited, current_path, simple_paths, edges):
    if visited[u]:
        # dead end, go back
        return
    if not u.isupper() and not u == 'end' :
        visited[u] = True
    current_path.append(u)
    if u == v:
        # a path has been found
        simple_paths.append(current_path.copy())
        current_path.pop(-1)
        return
    for neighbour in edges[u]:
        DFS(neighbour, v, visited, current_path, simple_paths, edges)
    current_path.pop(-1)
    visited[u] = False


def all_paths(edges):
    simple_paths = []
    current_path = []
    visited = dict.fromkeys(edges.keys(), False)
    DFS('start', 'end', visited, current_path, simple_paths, edges)
    return(len(simple_paths), simple_paths)

# Part 1
print(all_paths(graph_dict)[0])



# Part 2
# very stupid and slow solution, but I double each node and then calculate paths, remove doubles at the end
paths = all_paths(graph_dict)[1]
for elt in graph_dict:
    if elt.islower() and elt != 'start' and elt != 'end':
        # copy the original graph, the add copied node
        edge_copy = graph_dict.copy()
        neighbours = edge_copy[elt].copy()
        edge_copy[elt+"copy"] = neighbours
        # add copied node as neighbour
        for neighbour in neighbours:
            edge_copy[neighbour].append(elt+"copy")
        new_paths = all_paths(edge_copy)[1]

        for path in new_paths:
            # replace doubled node in path by original name
            for index in range(len(path)):
                if path[index] == elt+"copy":
                    path[index] = elt
            # and add to paths
            paths.append(path)

        for neighbour in neighbours:
            # for some reason, editing the copied dict's values also changes the values in the original dict
            # these "values" are the neighbours of a node, so manually remove the copied node each time
            graph_dict[neighbour].pop()
paths.sort()
unique_paths = list(paths for paths,_ in itertools.groupby(paths))
print(len(unique_paths))

