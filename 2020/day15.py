with open("data/input_for_day15.txt", "r") as f:
    numbers = f.readline().rstrip().split(",")

previously_called = {}
for turn in range(len(numbers)):
    previously_called[int(numbers[turn])] = (turn, turn)

last = numbers[-1]
exercise1 = 2020
exercise2 = 30000000
for turn in range(len(numbers), exercise2):
    if last in previously_called:
        next = previously_called[last][0] - previously_called[last][1]
    else:
        next = 0
    if next in previously_called:
        current = previously_called[next]
        previously_called[next] = (turn, current[0])
    else:
        previously_called[next] = (turn, turn)
    last = next
print(next)