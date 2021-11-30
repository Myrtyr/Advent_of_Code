with open("data/input_for_day7.txt", "r") as f:
    text = f.readlines()

color_bags = {}
for line in text:
    bigbag, contains = line.split("contain")
    bigbag_colortype, bigbag_color, rest, rest = bigbag.split(" ")
    bigbag = bigbag_colortype + bigbag_color
    contains_bags = contains.split(",")
    littlebags = {}
    for bag in contains_bags:
        littlebag_info = bag.split(" ")
        littlebag_color = littlebag_info[2] + littlebag_info[3]
        littlebag_amount = littlebag_info[1]
        littlebags[littlebag_color] = littlebag_amount
    color_bags[bigbag] = littlebags

result = {"shinigold"}
containing_gold = ["shinygold"]
while containing_gold:
    # find all bags that can contain shinygold
    # update containing_gold to those bags
    # remove shinygold from list
    new_containing_gold = []
    for bag in color_bags:
        # check if containing_gold and color_bags[bag]
        # have any overlap, if so, add bag to new_...
        for gold_bag in containing_gold:
            if gold_bag in color_bags[bag]:
                result.add(bag)
                new_containing_gold.append(bag)
    containing_gold = new_containing_gold
print(len(result)-1)


def bags_in_bag(bag):
    if color_bags[bag] == {'otherbags.\n': 'no'}:
        return 1
    else:
        print(bag, color_bags[bag])
        return sum(int(color_bags[bag][bag2])*bags_in_bag(bag2) for bag2 in color_bags[bag])+1  #count bag we just visited too
print(bags_in_bag('shinygold')-1)   #shiny gold bag is not contained in itself
