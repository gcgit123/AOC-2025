'''
Day 10
'''

with open("input10") as f:
    machines = f.readlines()

for i in range(len(machines)):
    machines[i] = machines[i][:-1]
    machines[i] = machines[i].split(" ")
    for j in range(len(machines[i])):
        machines[i][j] = machines[i][j][1:-1].split(',')

for i in range(len(machines)):
    machines[i][0] = [x for x in machines[i][0][0]]
    

#part 1
import collections


total = 0
for i in range(len(machines)):
    starting_point = ['.'] * len(machines[i][0]) 
    seen = set()
    seen.add(tuple(starting_point))

    q = collections.deque([[x, starting_point[:], 0] for x in machines[i][1:-1]])

    while q:
        button, lights, steps = q.popleft()

        nlights = lights[:]

        for light in button:
            if nlights[int(light)] == '.':
                nlights[int(light)] = '#'
            else:
                nlights[int(light)] = '.'   

        if nlights == machines[i][0]:
            total += (steps+1)
            break
        if tuple(nlights) in seen:
            continue
        else:
            seen.add(tuple(nlights))

        for b in machines[i][1:-1]:
            q.append([b[:], nlights[:], steps+1])

print("Answer is: ",total )

#part 2 bsf too slow
total2 = 0
for i in range(len(machines)):

    starting_point2 = [0]*len(machines[i][-1])

    q2 = collections.deque([[x, starting_point2[:], 0] for x in machines[i][1:-1]])

    seen = set()
    seen.add(tuple(starting_point2))

    target = [int(x) for x in machines[i][-1]]

    while q2:

        buttons, jolts, steps = q2.popleft()
        njolts = jolts[:]

        for j in buttons:
            njolts[int(j)] += 1
        
        if njolts == target:
            total2 += (steps+1)
            break

        if tuple(njolts) in seen:
            continue
        else:
            seen.add(tuple(njolts))

        for j in range(len(njolts)):
            if njolts[j] > target[j]:
                continue



        for b in machines[i][1:-1]:
            q2.append([b[:], njolts[:], steps+1])

    print(i, total2, steps+1)    

print("Answer is: ", total2)


#part 2 again dfs still too slow

     
from functools import cache


target = [int(x) for x in machines[1][-1]]

@cache
def dfs(joltage, steps):
    joltage = list(joltage)  

    buttons = machines[1][1:-1]

    if joltage == target:
        return steps

    for k in range(len(joltage)):
        if joltage[k] > target[k]:
            return float('inf')  

    best = float('inf')
    for b in buttons:
        new_jolts = joltage[:]
        for j in b:
            new_jolts[int(j)] += 1
        best = min(best, dfs(tuple(new_jolts), steps + 1)) 

    return best

result = dfs(tuple([0]*len(machines[1][-1])), 0)
print(result)


