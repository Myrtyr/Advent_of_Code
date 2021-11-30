with open("data/input_for_day5.txt", "r") as f:
    text = f.read()
    texts = text.split("\n")


def sequence_to_binary(sequence):
    binary_row = ''
    binary_col = ''
    for character in sequence:
        if character == 'B':
            binary_row += '1'
        elif character == 'F':
            binary_row += '0'
        elif character == 'R':
            binary_col += '1'
        elif character == 'L':
            binary_col += '0'
    return binary_row, binary_col

def sequences_to_id(texts):
    max = 0
    for sequence in texts:
        row, col = sequence_to_binary(sequence)
        if 8*int(row,2)+int(col,2) > max:
            max = 8*int(row,2)+int(col,2)
    return max

def sequences_to_my_id(texts):
    ids = []
    for sequence in texts:
        row, col = sequence_to_binary(sequence)
        ids.append(8*int(row,2)+int(col,2))
    ids.sort()
    prev = ids[0]
    for i in range(len(ids)-1):
        if ids[i-1] != ids[i]-1 or ids[i]+1 != ids[i+1]:
            print(ids[i])
    return ids

print(sequences_to_my_id(texts[:-1]))