with open("data/input_for_day18.txt", "r") as f:
    lines = f.readlines()


def addition(entire_sum):
    if len(entire_sum) == 1:
        return int(entire_sum)
    # there must be a bracket
    elif entire_sum[-1] == ")":
        haakjesverschil = 1
        left_index = -1
        while haakjesverschil != 0:
            left_index -= 1
            if entire_sum[left_index] == "(":
                haakjesverschil -= 1
            elif entire_sum[left_index] == ")":
                haakjesverschil += 1
        if abs(left_index) >= len(entire_sum):
            # if the brackets are the last thing
            return addition(entire_sum[left_index + 1:-1])
        else:
            operation_after_bracket = entire_sum[left_index-1]
            if operation_after_bracket == "+":
                return addition(entire_sum[left_index+1:-1]) + addition(entire_sum[:left_index-1])
            elif operation_after_bracket == "*":
                return addition(entire_sum[left_index+1:-1]) * addition(entire_sum[:left_index-1])
            else:
                print("I missed another something")
    elif entire_sum[-1].isdigit():
        if entire_sum[-2] == "*":
            return int(entire_sum[-1]) * addition(entire_sum[:-2])
        elif entire_sum[-2] == "+":
            return int(entire_sum[-1]) + addition(entire_sum[:-2])
        else:
            # bracket?
            print("I missed something here", entire_sum)
    else:
        print("I missed something", entire_sum)

res = 0
for line in lines:
    line = line.rstrip().replace(" ", "")
    # print(line)
    # print(addition(line))
    res += addition(line)
print(res)


def add_some_brackets(one_line):
    new_line = one_line
    elt_index = 0
    while elt_index < len(new_line):
        elt = new_line[elt_index]
        if elt == "+":
            # first left side
            if new_line[elt_index-1].isdigit():
                # add bracket to left of digit
                left_index = elt_index - 1
            else:
                # first find out where brackets end
                haakjesverschil = 1
                left_index = elt_index - 1
                while haakjesverschil != 0:
                    left_index -= 1
                    if new_line[left_index] == "(":
                        haakjesverschil -= 1
                    elif new_line[left_index] == ")":
                        haakjesverschil += 1
            # then right side
            if new_line[elt_index + 1].isdigit():
                # add bracket to right of digit
                right_index = elt_index + 1
            else:
                # first find out where brackets end
                haakjesverschil = 1
                right_index = elt_index + 1
                while haakjesverschil != 0:
                    right_index += 1
                    if new_line[right_index] == "(":
                        haakjesverschil += 1
                    elif new_line[right_index] == ")":
                        haakjesverschil -= 1
            change = new_line[:left_index]+"("+new_line[left_index:right_index+1]+")"+new_line[right_index+1:]
            new_line = change
            elt_index += 1
        elt_index += 1
    return new_line

res2 = 0
for line in lines:
    line = line.rstrip().replace(" ", "")
    with_brackets = add_some_brackets(line)
    res2 += addition(with_brackets)
print(res2)