from collections import deque

stack_1 = deque([])
stack_2 = deque([])

with open("data/input_for_day22.txt", "r") as f:
    data_1, data_2 = f.read().split("\n\n")
data_1 = data_1[1:].split("\n")
data_2 = data_2[1:].split("\n")
# for line in data_1:
#     line = line.rstrip()
#     if line.isdigit():
#         stack_1.append(int(line))
# for line in data_2:
#     line = line.rstrip()
#     if line.isdigit():
#         stack_2.append(int(line))
#
# while stack_1 and stack_2:
#     card_1 = stack_1.popleft()
#     card_2 = stack_2.popleft()
#     if card_1 > card_2:
#         stack_1.extend([card_1, card_2])
#     else:
#         stack_2.extend([card_2, card_1])
# if stack_1:
#     winner = stack_1
# else:
#     winner = stack_2
#
# score = 0
# amount_of_cards = len(winner)
# for i in range(1,amount_of_cards+1):
#     score += i*winner.pop()
# print(score)

#### NEW GAME ####
player_1 = deque([])
player_2 = deque([])
for line in data_1:
    line = line.rstrip()
    if line.isdigit():
        player_1.append(int(line))
for line in data_2:
    line = line.rstrip()
    if line.isdigit():
        player_2.append(int(line))

def recursive_game(stack_1, stack_2):
    al_geweest = []
    while stack_1 and stack_2:
        if (stack_1, stack_2) in al_geweest:
            return "1"
        al_geweest.append((stack_1.copy(), stack_2.copy()))
        card_1 = stack_1.popleft()
        card_2 = stack_2.popleft()
        len_1 = len(stack_1)
        len_2 = len(stack_2)
        if card_1 <= len_1 and card_2 <= len_2:
            # start the recursive game
            new_stack_1 = deque([])
            new_stack_2 = deque([])
            for i in range(card_1):
                new_stack_1.append(stack_1[i])
            for i in range(card_2):
                new_stack_2.append(stack_2[i])
            # recursive call
            winner_sub = recursive_game(new_stack_1, new_stack_2)
            if winner_sub == "1":
                stack_1.extend([card_1, card_2])
            else:
                stack_2.extend([card_2, card_1])
        else:
            if card_1 > card_2:
                stack_1.extend([card_1, card_2])
            else:
                stack_2.extend([card_2, card_1])
    if stack_1:
        winner = "1"
    else:
        winner = "2"
    return winner

if recursive_game(player_1, player_2) == "1":
    winner = player_1
else:
    winner = player_2
score = 0
amount_of_cards = len(winner)
for i in range(1,amount_of_cards+1):
    score += i*winner.pop()
print(score)