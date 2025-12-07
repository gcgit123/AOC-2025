'''
Day 7
'''

with open("input7") as f:
    teleporter = f.readlines()

for i in range(len(teleporter)):
    teleporter[i] = teleporter[i][:-1]

#Part 1

splits = 0

seen = set()
def dfs(x, y):
    global splits
    if (x,y) in seen:
        return
    else:
        seen.add((x,y))

    if y == len(teleporter):
        return 
    if x == len(teleporter[0]) or x == -1:
        return
    if teleporter[y][x] == "^":
        splits +=1 
        dfs(x+1, y+1)
        dfs(x-1, y+1)
    else:
        dfs(x, y+1)
    
    

dfs(70, 0)

print("The number of splits is: ", splits)

#Part 2

tp_prac = ['.......S.......','...............','.......^.......','...............','......^.^......','...............','.....^.^.^.....','...............','....^.^...^....','...............','...^.^...^.^...','...............','..^...^.....^..','...............','.^.^.^.^.^...^.','...............']


curr  = [0] * len(teleporter[0])
curr[70] = 1

m = len(teleporter)
n = len(teleporter[0])

def valid(x, y):
    return 0<= x < n and 0<=y<m


for j in range(m):
    next = [0] * n
    for i in range(n):
        if valid(i, j):
            if teleporter[j][i] == "^":
                next[i+1] += curr[i]
                next[i-1] += curr[i]
            else:
                next[i] += curr[i]    
    curr = next[:]

print("The amount of timelines is: ", sum(curr))


