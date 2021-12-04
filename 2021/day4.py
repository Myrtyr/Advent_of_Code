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
        numbers = row.split()
        all_bingo_cards[-1].append(numbers)

for number in order:
    for bingo_card in all_bingo_cards:
        print(bingo_card)
        for row_index in range(len(bingo_card)):
            row = bingo_card[row_index]
            for col_index in range(len(row)):
                if row[col_index] == number:
                    bingo_card[row_index][col_index] = 0
        for col_index in range(len(row)):

        for row_index in range(len(bingo_card)):
            row = bingo_card[row_index]

            if not row:
                bingo_card.remove([])
                remaining = [int(item) for items in bingo_card for item in items]
                print(remaining, number)
                start = 0
                for elt in remaining:
                    start += elt
                print("There's a winner, with a score of: ", int(number)*start)
                break
        else:
            continue
        break
    else:
        continue
    break

