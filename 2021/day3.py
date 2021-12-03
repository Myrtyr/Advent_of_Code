import numpy as np


with open("2021/data/input_day3.txt", "r") as f:
    lines = f.readlines()


# Puzzle 1
# First I make a matrix of all binary bits
binary_strings = np.zeros((len(lines), len(lines[0])-1))
for index in range(len(lines)):
    number = lines[index]
    for subindex in range(len(number)-1):
        bit = number[subindex]
        binary_strings[index,subindex] = int(bit)
# Then I determine the most frequent bit at each position
gamma = ""
for index in range(len(binary_strings[0])):
    newbit = str(round(sum(binary_strings[:, index]) / len(binary_strings)))
    gamma += newbit
# Finally calculate product
eps = 2**(len(gamma)) - int(gamma,2) - 1
print(int(gamma,2),eps, eps*int(gamma,2))

# Puzzle 2

# oxygen generator rating
length = len(binary_strings[0])
rows = len(binary_strings)
answers_oxygen = [True] * (len(binary_strings))
index = 0
while (answers_oxygen.count(True) > 1):
    intermediate = sum(binary_strings[answers_oxygen, index]) / len(binary_strings[answers_oxygen])
    newbit = int(intermediate>=0.5)
    for row_index in range(rows):
        elt = binary_strings[row_index, index]
        if newbit != elt:
            answers_oxygen[row_index] = False
    index += 1
final_answer_oxygen = ""
for elt in binary_strings[answers_oxygen][0]:
    final_answer_oxygen += str(int(elt))
print("C02", int(final_answer_oxygen,2))

# CO2
answers_c02 = [True] * (len(binary_strings))
index = 0
while (answers_c02.count(True) > 1):
    intermediate = sum(binary_strings[answers_c02, index]) / len(binary_strings[answers_c02])
    newbit = 1-int(intermediate>=0.5)
    for row_index in range(rows):
        elt = binary_strings[row_index, index]
        if newbit != elt:
            answers_c02[row_index] = False
    index += 1
final_answer_c02 = ""
for elt in binary_strings[answers_c02][0]:
    final_answer_c02 += str(int(elt))
print("C02", int(final_answer_c02,2))
