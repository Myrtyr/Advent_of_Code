with open("data/input_for_day13.txt", "r") as f:
    eta = int(f.readline().rstrip())
    busnumbers = f.readline().rstrip()

buses1 = busnumbers.replace("x", "").split(",")
buses1 = [int(x) for x in buses1 if x]
print(buses1)

for i in range(100):
    time = eta + i
    if any([time % bustime == 0 for bustime in buses1]):
        print([time % bustime == 0 for bustime in buses1])
        print(i)
        break


def euclidean_algorithm(larger, smaller):
    s_1 = 1
    s_2 = 0
    t_1 = 0
    t_2 = 1
    r_1 = s_1 * larger + t_1 * smaller
    r_2 = s_2 * larger + t_2 * smaller
    r_3 = larger - smaller
    while r_3 != 0:
        quotient = int(r_1 / r_2)
        r_3 = r_1 - quotient * r_2
        s_3 = s_1 - quotient * s_2
        t_3 = t_1 - quotient * t_2
        r_1, s_1, t_1 = r_2, s_2, t_2
        r_2, s_2, t_2 = r_3, s_3, t_3
    print(s_1, "*", larger, "+", t_1, "*", smaller, "=", s_1*larger+t_1*smaller)
    return s_1

buses2 = busnumbers.split(",")
offsets = []
for i in range(len(buses2)):
    if buses2[i] != "x":
        offsets.append(-int(i))
actual_offsets = [offsets[index] % buses1[index] for index in range(len(buses1))]
print(actual_offsets)
print(buses1)

N = 1
for number in buses1:
    N *= number
print("Een bovengrens is: ", N)

x_list = []
for i in range(len(buses1)):
    smaller_one = buses1[i]
    larger_one = int(N / buses1[i])
    # do euclidean algorithm on smaller and larger
    new_s = euclidean_algorithm(larger_one, smaller_one)
    new_x = actual_offsets[i]*new_s*larger_one
    x_list.append(new_x)
print(sum(x_list)%N)
