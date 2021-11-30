with open("data/input_for_day1.txt") as file:
    data = file.read()
    data = data.split()

it = 0
for i in data:
    it += 1
    it2 = it
    for j in data[it:]:
        it2 += 1
        for z in data[it2:]:
            if int(z)+int(i)+int(j) == 2020:
                print(int(z)*int(i)*int(j))




