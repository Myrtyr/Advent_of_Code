with open("2021/data/input_day6.txt", "r") as f:
     first_line = f.readline().split(",")
     fish_start = [int(item) for item in first_line]

days = 256

for day in range(days):
     new_fish = []
     for fish_index in range(len(fish_start)):
          fish_timer = fish_start[fish_index]
          if fish_timer == 0:
               fish_start[fish_index] = 6
               new_fish.append(8)
          else:
               fish_start[fish_index] -= 1
     fish_start += new_fish
print(len(fish_start))

# Puzzle 2
# fish_total = 0
# while not fish_start:
#      current_fish = fish_start[0]
#      new_births = (80-current_fish)/7
#      remainder = (80-current_fish)%7
#
#
#      fish_start.pop(0)

