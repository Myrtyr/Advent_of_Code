import numpy as np

with open ("2021/data/input_day4.txt", "r") as f:
    order = f.readline()[:-1].split(",")
    f.readline()
    bingo_cards = f.read()[:-1].split("\n\n")

all_bingo_cards = []
for bingo_card in bingo_cards:
    rows = bingo_card.split("\n")
    to_append = []
    for row in rows:
        to_append.append([])
        numbers = row.split()
        for number in numbers:
            to_append[-1].append(int(number))
    all_bingo_cards.append(np.array(to_append))


def finish_game(bingo_card):
    remaining = [int(item) for items in bingo_card for item in items]
    start = 0
    for elt in remaining:
        start += elt
    score = int(number) * start
    print("There's a winner, with a score of: ", score)
    return score

for number in order:
    for index in range(len(all_bingo_cards)):
        bingo_card = all_bingo_cards[index]
        for row_index in range(len(bingo_card)):
            row = bingo_card[row_index]
            for col_index in range(len(row)):
                if row[col_index] == int(number):
                    bingo_card[row_index][col_index] = 0
        for col_index in range(len(row)):
            if sum(bingo_card[:,col_index]) == 0:
                finish_game(bingo_card)
                all_bingo_cards[index] = 100*np.ones((5,5))

        for row_index in range(len(bingo_card)):
            if sum(bingo_card[row_index,:]) == 0:
                finish_game(bingo_card)
                all_bingo_cards[index] = 100*np.ones((5,5))

