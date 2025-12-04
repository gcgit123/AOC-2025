'''
Day 4
'''


with open("input4") as input4:
    grid = input4.readlines()

for i in range(len(grid)):
    grid[i] = [x for x in grid[i][:-1]]


'''
practice = ['..@@.@@@@.', '@@@.@.@.@@','@@@@@.@.@@','@.@@@@..@.','@@.@@@@.@@','.@@@@@@@.@','.@.@.@.@@@','@.@@@.@@@@','.@@@@@@@@.','@.@.@@@.@.']
for i in range(len(practice)):
    practice[i] = [x for x in practice[i]]
'''

#Part 1
directions = [(0,1), (1,0), (0,-1), (-1, 0), (1,1), (-1,-1), (1, -1), (-1, 1)]
m = len(grid[0])
n = len(grid)
def isvalid(x, y):
    return 0<=x<m and  0<=y<n

good_roll = 0
for i in range(m):
    for j in range(n):
        count = 0
        if grid[i][j] == "@":
            for x, y in directions:
                new_x = x+i
                new_y = y+j
                if isvalid(new_x, new_y) and grid[new_x][new_y] == "@":
                    count +=1
            if count < 4:
                good_roll += 1
        
print("number of good rolls is: ", good_roll)


#Part 2
'''
practice = ['..@@.@@@@.', '@@@.@.@.@@','@@@@@.@.@@','@.@@@@..@.','@@.@@@@.@@','.@@@@@@@.@','.@.@.@.@@@','@.@@@.@@@@','.@@@@@@@@.','@.@.@@@.@.']
for i in range(len(practice)):
    practice[i] = [x for x in practice[i]]
'''

m= len(grid)
n = len(grid[0])

def isvalid(x, y):
    return 0<=x<m and  0<=y<n

directions = [(0,1), (1,0), (0,-1), (-1, 0), (1,1), (-1,-1), (1, -1), (-1, 1)]

removed = 0
remove = 1
while remove > 0:
    remove = 0
    for i in range(m):
        for j in range(n):
            count = 0
            if grid[i][j] == "@":
                for x, y in directions:
                    new_x = x+i
                    new_y = y+j
                    if isvalid(new_x, new_y) and grid[new_x][new_y] == "@":
                        count +=1
                if count < 4:
                    grid[i][j] = "X"
                    removed += 1
                    remove += 1

print('The amount removed is: ', removed)
                   





