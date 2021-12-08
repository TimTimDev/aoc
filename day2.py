f = open("inputs/day2_input.txt", "r")

horizontal = 0
depth = 0
aim = 0

# Turn inputs into list 
list_of_lists = []
for line in f:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

f.close()

# Turn stringed numbers into integers and check if horizontal or up or down is in the list
# and if they are in the list, add according integer to appropriate value
for i in range(len(list_of_lists)):
    inted = int(list_of_lists[i][1])
    
    if "forward" in list_of_lists[i]:
        horizontal = horizontal + inted
        depth =  depth + (inted * aim)
    elif "up" in list_of_lists[i]:
        # depth = depth - inted
        aim = aim - inted
    else:
        # depth = depth + inted
        aim = aim + inted

# Multiply horizontal and depth value to get final answer
final = horizontal * depth
print(final)
