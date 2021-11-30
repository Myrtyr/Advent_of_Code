with open("data/input_for_day9.txt", "r") as f:
    text_file = f.readlines()
number_list = []
for i in range(1000):
    number_list.append(int(text_file[i].rstrip()))


def add_check(number_list, number):
    for elt in number_list:
        remainder = number - elt
        if remainder in number_list and remainder != elt:
            return True
    return False


def find_invalid():
    previous = []
    for i in range(25):
        previous.append(number_list[i])
    for i in range(25, len(number_list)):
        line = number_list[i]
        if not (add_check(previous, line)):
            return(line)
        previous.append(line)
        previous.pop(0)
    return "no problems"

print(find_invalid())

def find_contiguous():
    sum_set = []
    goal_number = find_invalid()
    current = 0
    while sum(sum_set) != goal_number:
        if sum(sum_set) > goal_number:
            sum_set.pop(0)
        else:
            sum_set.append(number_list[current])
            current += 1
    return sum_set

print(find_contiguous())

def calculate_weakness():
    weakness_list = find_contiguous()
    weakness_list.sort()
    return weakness_list[0] + weakness_list[-1]

print(calculate_weakness())