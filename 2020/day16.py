with open("data/input_for_day16.txt", "r") as f:
    text = f.read()

rules, myticket, othertickets = text.split("\n\n")

correct = []
rules = rules.split("\n")
for rule in rules:
    numbers = rule.split(":")[1]
    words = numbers.split(" ")
    range1start, range1end = words[1].split("-")
    range2start, range2end = words[3].split("-")
    for i in range(int(range1start), int(range1end)+1):
        if i not in correct:
            correct.append(i)
    for i in range(int(range2start), int(range2end)+1):
        if i not in correct:
            correct.append(i)

othertickets = othertickets.split("\n")[1:]
newtickets = []
for elt in othertickets:
    newtickets += elt.split(",")
wrong = 0
for elt in newtickets:
    if elt.isdigit():
        if int(elt) not in correct:
            wrong += int(elt)
print(wrong)

newnewtickets = []
for ticket in othertickets[:-1]:
    values = ticket.split(",")
    if all([int(value) in correct for value in values]):
        newnewtickets.append(ticket)

rule_dict = {}
for rule in rules:
    newcorrectlist = []
    name, numbers = rule.split(": ")
    boundaries = numbers.split(" or ")
    for boundary in boundaries:
        start, stop = boundary.split("-")
        for i in range(int(start), int(stop)+1):
            if i not in newcorrectlist:
                newcorrectlist.append(i)
    rule_dict[name] = newcorrectlist

try_this_dict = {}
for rulename, rulevalues in rule_dict.items():
    try_this_dict[rulename] = [0]*20
    for ticket in newnewtickets:
        values = ticket.split(",")
        for j in range(len(values)):
            if int(values[j]) not in rulevalues:
                try_this_dict[rulename][j] += 1

for name, values in try_this_dict.items():
    print(20-sum(values), name, [i for i in range(len(values)) if values[i] == 0])

myticket_values = myticket.split("\n")[1].split(",")
indices = [2, 9, 10, 17, 18, 19]
finally_correct_values = [int(myticket_values[ind]) for ind in indices]
first = 1
for cijfer in finally_correct_values:
    first *= cijfer
print(first)