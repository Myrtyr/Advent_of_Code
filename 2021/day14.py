import copy

# reading file
with open("2021/data/input_day14.txt", "r") as f:
    start_string = f.readline().rstrip()
    f.readline()
    insertions = f.readlines()
another_start_string = start_string

insertion_dict = {}
for insertion in insertions:
    insertion_from, insertion_to = insertion.rstrip().split(" -> ")
    insertion_dict[insertion_from] = insertion_to

def max_min_min(dict):
    max_val = max(dict, key=dict.get)
    min_val = min(dict, key=dict.get)
    diff = dict[max_val] - dict[min_val]
    return diff


def single_step(start):
    new_string = ""
    for index in range(len(start) - 1):
        pair = start[index:index + 2]
        new_string += start[index]
        new_string += insertion_dict[pair]
    new_string += start[-1]
    return new_string

# Puzzle 1
for i in range(10):
    start_string = single_step(start_string)

a = {}
for character in start_string:
    a[character] = start_string.count(character)
print(max_min_min(a))

# Puzzle 2 (could be used for part 1 as well
all_characters = ["K", "P", "C", "V", "B", "F", "O", "S", "N", "H"]
solution_dict = {}
for character in all_characters:
    solution_dict[character] = dict.fromkeys(all_characters, 0)
for index in range(len(another_start_string)-1):
    current = another_start_string[index]
    next = another_start_string[index+1]
    solution_dict[current][next] += 1


def single_step_dict(start_dict):
    finished_dict = copy.deepcopy(start_dict)
    for character_left in start_dict:
        for character_right in start_dict[character_left]:
            insertion = insertion_dict[character_left+character_right]
            occurrences = start_dict[character_left][character_right]
            finished_dict[character_left][insertion] += occurrences
            finished_dict[character_left][character_right] -= occurrences
            finished_dict[insertion][character_right] += occurrences
    return finished_dict


def count_occurrences_dict(finished_dict):
    temp_dict = dict.fromkeys(all_characters,0)
    # calculate occurrences by counting how many 'next's it has
    for letter in all_characters:
        for key in finished_dict[letter]:
            temp_dict[letter] += finished_dict[letter][key]
    # probably won't matter, but the final letter has no next, so is counted once less above
    temp_dict[another_start_string[-1]] += 1
    return temp_dict


for i in range(40):
    solution_dict = single_step_dict(solution_dict)
print(max_min_min(count_occurrences_dict(solution_dict)))