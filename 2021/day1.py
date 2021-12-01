with open("2021/data/input_day1.txt", "r") as f:
    depths_raw = f.readlines()

counter = 0
start = int(depths_raw[0])
for depth in depths_raw:
    next = int(depth)
    if next > start:
        counter += 1
    start = next
print(counter)

counter = 0
start = int(depths_raw[0])
mid = int(depths_raw[1])
end = int(depths_raw[2])
for depth in depths_raw:
    next = int(depth)
    old = start + mid + end
    new = old - start + next
    if new > old:
        counter += 1
    start = mid
    mid = end
    end = next
print(counter)