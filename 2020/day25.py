# actual input values
input_A = 3418282
input_B = 8719412
subject_number = 7
divide_by = 20201227

# example values
public_key_card = 5764801
public_key_door = 17807724
loop_size_card = 8
loop_size_door = 11

# determine loop size for public key A
start = input_A
loop_size_A = 0
while start != 1:
    if start%subject_number == 0:
        start /= subject_number
        loop_size_A += 1
    else:
        start += divide_by
print(loop_size_A)
loop_size_A = 8987376

# determine loop size for public key B
start = input_B
loop_size_B = 0
while start != 1:
    if start%subject_number == 0:
        start /= subject_number
        loop_size_B += 1
    else:
        start += divide_by
print(loop_size_B)

# transform public key A according to loop size B
start = 1
for i in range(loop_size_B):
    start *= input_A
    start %= divide_by
print(start)

