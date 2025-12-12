'''
Day 12
'''

import math
with open("input12") as f:
    instructions = f.readlines()


instructions = [x for x in instructions if x != '\n']

instructions = [x[:-1] for x in instructions]


areas = []
for i in range(0, 24, 4):
    area = 0
    for x in range(i+1, i+4):
        area += instructions[x].count('#')
    areas.append(area)

for i in range(24, len(instructions)):
    instructions[i] = instructions[i].split(':')

for i in range(24, len(instructions)):
    instructions[i][0] = instructions[i][0].split('x')
    instructions[i][1] = instructions[i][1].strip().split(' ')


fits = 0
for i in range(24, len(instructions)):
    space = math.prod([int(x) for x in instructions[i][0]])
    pres_size = 0
    for j in range(len(instructions[i][1])):
        pres_size += (int(instructions[i][1][j]) * areas[j])
    if pres_size <= space:
        fits +=1

print('The total amount of presents that fits are:', fits)