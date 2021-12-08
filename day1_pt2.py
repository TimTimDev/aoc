f = open("inputs/day1_pt2_input.txt", "r")

listy = []

i = 0
next_sum = 0
num_of_incs = 0


# Loop through file and append values to list

for x in f:
    stripped_x = x.strip()
    listy.append(stripped_x)

print(listy)

while i < len(listy) - 3:
    summy = int(listy[i]) + int(listy[i+1]) + int(listy[i+2])
    next_sum = int(listy[i+1]) + int(listy[i+2]) + int(listy[i+3])
    i += 1

    print(summy, next_sum)

    if next_sum > summy:
        num_of_incs += 1
    
    


print(num_of_incs)



f.close()
