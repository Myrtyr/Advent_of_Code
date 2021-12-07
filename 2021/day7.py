with open("2021/data/input_day7.txt", "r") as f:
    numbers_as_string = f.readline()
numbers = [int(number) for number in numbers_as_string.split(",")]
print(len(numbers))
# Puzzle 1
median = sorted(numbers)[int(len(numbers)/2)]
distances = 0
for elt in numbers:
    distances += abs(elt-median)
print(distances)

# Puzzle 2
avg = int(sum(numbers)/len(numbers))

distances = 0
for elt in numbers:
    distances += sum(range(abs(elt-avg)+1))
print(distances)

