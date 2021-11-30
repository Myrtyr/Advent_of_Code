with open("data/day 10 puzzle 1 data.txt") as f:
    text = f.readlines()

numbers = []
for line in text:
    numbers.append(int(line.rstrip()))
numbers.sort()

necessary = []
optional = []
ones = 0
twos = 0
threes = 0
previous = 0
for number in numbers:
    if number - previous == 1:
        ones += 1
    elif number - previous == 2:
        twos += 1
    elif number - previous == 3:
        threes += 1
        necessary.append(previous)
        necessary.append(number)
    else:
        print("oops")
    previous = number
threes += 1

print(ones*threes)
optional = [number for number in numbers if number not in necessary]
print(necessary)
print(len(optional))
print(len(numbers) - len(optional))


