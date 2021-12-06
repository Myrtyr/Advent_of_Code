with open("2021/data/input_day6.txt", "r") as f:
     first_line = f.readline().split(",")
     fish_start = [int(item) for item in first_line]

# puzzle 1
def calculate_fishes(fish_st, days):
     # very ugly function, it edits the fish_st list so problems
     for day in range(days):
          new_fish = []
          for fish_index in range(len(fish_st)):
               fish_timer = fish_st[fish_index]
               if fish_timer == 0:
                    fish_st[fish_index] = 6
                    new_fish.append(8)
               else:
                    fish_st[fish_index] -= 1
          fish_st += new_fish
     return len(fish_st)


# Puzzle 2 (can also be puzzle 1)
fish_amounts = [fish_start.count(0), fish_start.count(1), fish_start.count(2), fish_start.count(3), fish_start.count(4), fish_start.count(5), fish_start.count(6), fish_start.count(7), fish_start.count(8)]

for i in range(256):
     spawning = fish_amounts.pop(0)
     fish_amounts.append(spawning)
     fish_amounts[6] += spawning
print(sum(fish_amounts))



