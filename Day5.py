'''
Day 5
'''


with open("input5") as f:
    file = f.readlines()


file[187]

for i in range(len(file)):
    file[i] = file[i][:-1]

for i in range(187):
    file[i] = file[i].split("-")
    
for i in range(187):
    file[i][0] = int(file[i][0])
    file[i][1] = int(file[i][1])

for i in range(188, len(file)):
    file[i] = int(file[i])
    
ranges = file[:187]
nums = file[188:]

#Part 1

count = 0

for num in nums:
    for range in ranges:
        if range[0] <= num <= range[1]:
            count +=1
            break
    
print("There are ", count, "fresh ingredients")

#Part 2

ranges2 = sorted(ranges, key = lambda x: x[0])

new = [[None, None]] 
j = 0
i = 0
while j < len(ranges2):
    new[i] = [ranges2[j][0], ranges2[j][1]]
    j+=1
    while j < len(ranges2) and new[i][1] >= ranges2[j][0]:
        if new[i][1] <= ranges2[j][1]:
            new[i][1] = ranges2[j][1]
        j+=1
    new.append([None, None])
    i+=1


total = 0
for i in range(len(new)-1):
    total += len(range(new[i][0], new[i][1]+1))

print("The total fresh ingredients is: ", total)




   


