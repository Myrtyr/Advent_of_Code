with open('data/input_day1.txt', 'r') as f:
    depths_raw = f.readlines()

counter = 0
start = int(depths_raw[0])
for depth in depths_raw:
    next = int(depth)
    if next > start:
        counter += 1

print(counter)