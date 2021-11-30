with open("data/input_for_day8.txt", "r") as f:
    texts = f.readlines()
    texts.append("ja ?")

def once(text):
    visited = []
    current = 0
    accumulator = 0
    while current not in visited:
        line = text[current].rstrip()
        instruction, number = line.split(" ")
        visited.append(current)
        if instruction == "acc":
            accumulator += int(number)
            current += 1
        elif instruction == "jmp":
            current += int(number)
        elif instruction == "nop":
            current += 1
        else:
            print("The answer to exercise 2 is:", accumulator)
    return accumulator, current

print("The answer to exercise 1 is:", once(texts)[0])
nop_jmp = {"nop": "jmp", "jmp": "nop", "acc": "acc"}
for i in range(len(texts)-1):
    new_text = texts.copy()
    instruction, number = new_text[i].split(" ")
    new_text[i] = nop_jmp[instruction] + " " + number
    once(new_text)