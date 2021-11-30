from matplotlib.colors import is_color_like

with open("data/input_for_day4.txt", "r") as f:
    texts = f.read().split("\n")
passports = []
counter = 0
for i in range(len(texts)):
    if texts[i] == "":
        passports.append(texts[counter:i])
        counter = i+1

color_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid = 0
check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports:
    present = []
    is_valid = True
    for elt in passport:
        elt = elt.split(" ")
        for field in elt:
            category, value = field.split(":")
            present.append(category)
            if category == 'byr':
                if int(value) < 1920 or int(value) > 2002 or len(value) != 4:
                    is_valid = False
            if category == 'iyr':
                if int(value) < 2010 or int(value) > 2020 or len(value) != 4:
                    is_valid = False
            if category == 'eyr':
                if int(value) < 2020 or int(value) > 2030 or len(value) != 4:
                    is_valid = False
            if category == 'hgt':
                if value[-2:] == 'cm':
                    if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                        is_valid = False
                elif value[-2:] == 'in':
                    if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                        is_valid = False
                else:
                    is_valid = False
            if category == 'hcl':
                if not is_color_like(value):
                    is_valid = False
            if category == 'ecl':
                if not value in color_list:
                    is_valid = False
            if category == 'pid':
                if len(value) != 9 or not value.isdigit():
                    is_valid = False
    if not all(item in present for item in check):
        is_valid = False
    if not is_valid:
        print(passport)
    valid += is_valid
print(valid)