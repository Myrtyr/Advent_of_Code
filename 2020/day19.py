with open("data/small_input_for_day19.txt", "r") as f:
    text = f.read()

rules, received = text.split("\n\n")
received = received.split("\n")[:-1]

def make_rule_dict(rules):
    rule_dict = {}
    for rule in rules.split("\n"):
        rule_number, rule_matter = rule.split(": ")
        if rule_matter == '"a"':
            rule_stuff = "a"
        elif rule_matter == '"b"':
            rule_stuff = "b"
        else:
            rule_stuff = []
            for elt in rule_matter.split(" | "):
                rule_stuff.append(elt.split(" "))
        rule_dict[rule_number] = rule_stuff
    return rule_dict


def iterative_options():
    new_dict = {}
    while "0" not in new_dict.keys():
        print(new_dict)
        for rule_number, rule_value in rule_dict.items():
            if all([part.isalpha() for option in rule_value for part in option]):
                new_dict[rule_number] = rule_value
            # if only letters left, add to new dict
        for rulenumber, optionlist in new_dict.items():
            # replace numbers in ruledict with known options from newdict
            for rulenumber2change, optionlist2change in rule_dict.items():
                for option2change in optionlist2change:
                    for letter_index in range(len(option2change)):
                        current_letter = option2change[letter_index]
                        if current_letter == rulenumber:
                            # replace by all possible options
                            for option in optionlist:
                                option2change[letter_index] = option
                                # need to add the append at different moment?
                                rule_dict[rulenumber2change].append(option2change.copy())
    return new_dict


def recursive_options(rule_number):
    rule_value = rule_dict[rule_number]
    if rule_value != "a" and rule_value != "b":
        return [recursive_options(new_rule_number) for rule_seq in rule_dict[rule_number] for new_rule_number in rule_seq]
    else:
        return rule_value

# memory support
# for elt in output_from_stuff:
#     read_nonsense(elt)

def read_nonsense(options, output_list):
    if not output_list:
        # if there are no more letters to add, return all options
        return options
    if output_list[0] == "a" or output_list[0] == "b":
        # we have encountered a single letter which is necessary
        # so add letter to all options
        options = [option+output_list[0] for option in options]
        return read_nonsense(options, output_list[1:])
    else:
        # we have encountered a list
        # split into two options
        length_options = int(len(output_list[0])/2)
        option1 = output_list[0][:length_options]
        option2 = output_list[0][length_options:]
        if all(isinstance(val, str) for val in output_list[0]):
            options = 2 * options
            # add options
            for j in range(len(options)//2):
                for i in range(length_options):
                    options[j] += option1[i]
            for j in range(len(options)//2, len(options)):
                for i in range(length_options):
                    options[j] += option2[i]
            return read_nonsense(options, output_list[1:])
        else:
            return read_nonsense(options, option1) + read_nonsense(options, option2)
            # split into same two halves as in if
            # only now
            pass
    return options



def read_nonsense2(output_list):
    if not output_list:
        # if there are no more letters to add, return all options
        return []
    if output_list == "a" or output_list == "b":
        # we have encountered a single letter which is necessary
        # so add letter to all options
        return output_list
    else:
        # we have encountered a list
        # split into two options
        length_options = int(len(output_list)/2)
        option1 = output_list[:length_options]
        option2 = output_list[length_options:]
        if all(isinstance(val, str) for val in output_list):
            return ["".join(option1), "".join(option2)]
        else:
            option_list = []
            for elt in output_list:
                if isinstance(elt, list):
                    length_of_list = int(len(elt) / 2)
                    first = elt[:length_of_list]
                    second = elt[length_of_list:]
                    option_list.append(read_nonsense2(first))
                    option_list.append(read_nonsense2(second))
                else:
                    option_list.append(read_nonsense2(elt))
            return option_list
            # split into same two halves as in if
            # only now



def whatever(output_of_recursive):
    options = []
    ind = 0
    while any(isinstance(val, list) for val in output_of_recursive):
        current = output_of_recursive[ind]
        if type(current) == str:
            options = [option+current for option in options]
        elif type(current[0]) == str:
            options = 2*options
            length_options = int(len(current) / 2)
            option1 = current[:length_options]
            option2 = current[length_options:]
        ind += 1


# def fun(abc):
#     l = ['0']
#     start = ['']
#     it = 0
#     while l: #[[aa, aa]] of [[aaaa],[aaa]]
#         char = rule_dict[l.pop(-1)]
#         if len(char) == 1 and len(char[0]) == 2:
#             l.append(char[0][1])
#             l.append(char[0][0])
#         elif len(char) == 2: #or statement
#             l.append(char[1][1])
#             l.append(char[1][0])
#             l.append(char[0][1])
#             l.append(char[0][0])
#             start.append([start[-1]])
#             it += 1
#         elif len(char) == 1 and len(char[0]) == 1 and char[0][0] != "a"  and char[0][0] != "b":
#             l.append(char[0][0])
#         else:
#             pass
#     return start



rule_dict = make_rule_dict(rules)
# print(fun(rule_dict))
print(rule_dict)
print(iterative_options())
# print(recursive_options("0"))
# print("is my recursive function wrong?")
# print(read_nonsense2(recursive_options("0")))
# # print(whatever(recursive_options("0")))
