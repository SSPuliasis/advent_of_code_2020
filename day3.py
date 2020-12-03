lines = []
with open("aoc3.txt") as file :
 
    for line in file :
        line.strip()
        lines.append(line)

# PART 1     
trees = 0
clear = 0
position = 0
for line in lines:
    if position <= 30:
        if line[position] == '#':
            trees +=1
        elif line[position] == '.':
            clear +=1
        position +=3
    else:
        position -= 31
        if line[position] == '#':
            trees +=1
        elif line[position] == '.':
            clear +=1
        position +=3
     
     # PART 2
slope = 7
trees = 0
clear = 0
position = 0
for line in lines:
    if position <= 30:
        if line[position] == '#':
            trees +=1
        elif line[position] == '.':
            clear +=1
        position +=slope
    else:
        position -= 31
        if line[position] == '#':
            trees +=1
        elif line[position] == '.':
            clear +=1
        position +=slope
print('for slope = ', slope,' trees = ', trees)
 
#down 2
slope = 1
trees = 0
clear = 0
position = 0
for line in lines[::2]:
    if position <= 30:
        if line[position] == '#':
            trees +=1
        elif line[position] == '.':
            clear +=1
        position +=slope
    else:
        position -= 31
        if line[position] == '#':
            trees +=1
        elif line[position] == '.':
            clear +=1
        position +=slope
