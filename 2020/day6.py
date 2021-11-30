groups = []
yeses = ''
for line in open("data/input_for_day6.txt", "r"):
    if line == "\n":
        groups.append(yeses)
        yeses = ''
    for character in line[:-1]:
        if character not in yeses:
            yeses += character
groups.append(yeses)

total_sum = 0
for group in groups:
    total_sum += len(group)
print(total_sum)


groups = []
yeses = []
for line in open("data/input_for_day6.txt", "r"):
    if line == "\n":
        groups.append(yeses)
        yeses = []
    else:
        yeses.append(line[:-1])
groups.append(yeses)

res = 0
for group in groups:
    for character in group[0]:
        if all(character in others for others in group):
            res += 1
print(res)
