with open("2021/data/input_day10.txt", "r") as f:
    lines = f.readlines()

def incomplete_or_corrupted(line):
    corrupted = False
    index = 0
    opening_brackets = ['a']
    while not corrupted and index < len(line):
        bracket = line[index]
        if chr(ord(bracket)-2) == opening_brackets[-1] or chr(ord(bracket)-1) == opening_brackets[-1]:
            # always need to close last opening bracket first, otherwise
            opening_brackets.pop(-1)
        elif bracket == ")" or bracket == "}" or bracket == "]" or bracket == ">":
            # it's corrupted
            corrupted = True
        else:
            # must be an opening bracket
            opening_brackets.append(bracket)
        index += 1
    opening_brackets.pop(0)
    return corrupted, bracket, opening_brackets

auto_score = {"(": 1, "[": 2, "{": 3, "<": 4}

def auto_comp(missing_brackets):
    missing_brackets.reverse()
    score = 0
    for bracket in missing_brackets:
        score *= 5
        score += auto_score[bracket]
    return score


syntax_score = {")": 3, "]": 57, "}": 1197, ">": 25137}

score = 0
auto_completion_score = []
for line in lines:
    corrupted, bracket, missing = incomplete_or_corrupted(line)
    if corrupted:
        score += syntax_score[bracket]
    else:
        auto_completion_score.append(auto_comp(missing[:-1]))
print(score)
print(sorted(auto_completion_score)[int(len(auto_completion_score)/2)])


