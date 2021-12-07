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
avg = sum(numbers)/len(numbers)
check = 500
for index in range(len(numbers)):
    new_diff = abs(numbers[index] - avg)
    if new_diff < check:
        correct_index = index
        check = new_diff
avg = numbers[correct_index]
# turns out the number rounded down was in the list, so above can be replaced by avg = int(avg)
# but hey, this works every time

distances = 0
for elt in numbers:
    distances += sum(range(abs(elt-avg)+1))
print(distances)

