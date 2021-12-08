f = open("inputs/day1_pt1_input.txt", "r")

i = 0
depth_inc = 0

listy = []

# Loop through file and append values to list

for x in f:
    stripped_x = x.strip()
    listy_list = listy.append(stripped_x)

f.close()

for y in listy:
    inted_y = int(y)

    if inted_y > i:
        i=inted_y
        depth_inc += 1
    else:
        i = inted_y

print(depth_inc)