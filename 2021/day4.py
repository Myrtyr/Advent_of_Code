with open ("2021/data/input_day4.txt", "r") as f:
    order = f.readline()[:-1].split(",")
    f.readline()
    bingo_cards = f.read()[:-1].split("\n\n")
print(order)
all_bingo_cards = []
for bingo_card in bingo_cards:
    rows = bingo_card.split("\n")
    all_bingo_cards.append([])
    for row in rows:
        all_bingo_cards[-1].append([])
        numbers = row.split()
        for number in numbers:
            all_bingo_cards[-1][-1].append(int(number))

def finish_game(bingo_card):
    remaining = [int(item) for items in bingo_card for item in items]
    print(remaining, number)
    start = 0
    for elt in remaining:
        start += elt
    score = int(number) * start
    print("There's a winner, with a score of: ", score)
    return score

for number in order:
    print(number)
    for bingo_card in all_bingo_cards:
        for row_index in range(len(bingo_card)):
            row = bingo_card[row_index]
            for col_index in range(len(row)):
                if row[col_index] == int(number):
                    bingo_card[row_index][col_index] = 0
        for col_index in range(len(row)):
            if sum(bingo_card[:][col_index]) == 0:
                finish_game(bingo_card)
                break

        for row_index in range(len(bingo_card)):
            if sum(bingo_card[row_index][:]) == 0:
                finish_game(bingo_card)
                break
        else:
            continue
        break
    else:
        continue
    break
