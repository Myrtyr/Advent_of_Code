import numpy as np
import numpy.ma as ma

with open("data/input_for_day14.txt", "r") as f:
    text = f.readlines()

memory_positions = {}
for line in text:
    word, value = line.rstrip().split(" = ")
    if word == "mask":
        mask1 = int(value.replace("X", "1"), base=2)
        mask2 = int(value.replace("X", "0"), base=2)
    else:
        pos = int(word[4:-1])
        number = int(value) & mask1 # first remove all zeros
        number = number | mask2 # then add all ones
        memory_positions[pos] = number
print(sum(memory_positions.values()))

memory_positions = {}
for line in text:
    word, value = line.rstrip().split(" = ")
    if word == "mask":
        mask_float = int(value.replace("1", "0").replace("X", "1"), base=2)
        masklist = [mask_float]
        mask_normal = int(value.replace("X", "0"), base=2)
        flipbit = 1
        while flipbit < mask_float:
            for mask in masklist:
                new_mask = mask & ~flipbit
                if new_mask not in masklist:
                    masklist.append(new_mask)
            flipbit *= 2
    else:
        pos = int(word[4:-1]) | mask_normal
        number = int(value)
        memory_positions[pos] = number
        for mask in masklist:
            new_pos = pos ^ mask
            memory_positions[new_pos] = number
print(sum(memory_positions.values()))

