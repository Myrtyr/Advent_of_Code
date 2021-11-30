correct = 0
with open("data/input_for_day2.txt", "r") as f:
    for i in range(1000):
        line = f.readline()
        constraint, password = line.split(": ")
        password = password[:-1]
        constraint_amounts, constraint_letter = constraint.split(" ")
        constraint_min, constraint_max = constraint_amounts.split("-")
        amount = password.count(constraint_letter)
        if amount >= int(constraint_min) and amount <= int(constraint_max):
            correct += 1
print(correct)

correct2 = 0
with open("data/input_for_day2.txt", "r") as f:
    for i in range(1000):
        line = f.readline()
        constraint, password = line.split(": ")
        password = password[:-1]
        constraint_amounts, constraint_letter = constraint.split(" ")
        constraint_min, constraint_max = constraint_amounts.split("-")
        if (password[int(constraint_min)-1] == constraint_letter) ^ (password[int(constraint_max)-1] == constraint_letter):
            correct2 += 1
print(correct2)
