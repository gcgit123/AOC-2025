'''
Day3
'''

with open("input3") as f:
    banks = f.readlines()

for i in range(len(banks)):
    banks[i] = banks[i][:-1]



banks_prac = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']

#Part 1
n = len(banks[0])

def findlargest(nums):
    nums = [int(x) for x in nums]
    first = float('-inf')
    for i in range(len(nums)):
        num = nums[i]
        if num > first:
            first = num
            start = i
    if start < n-1:
        snd = max(nums[start+ 1:])
    else:
        snd = first
        first = max(nums[:-1])

    return first, snd


summer = 0
for bank in banks:
    frst, snd = findlargest(bank)
    summer += int(''.join([str(frst), str(snd)]))

print("The code is: ", summer)
        
#Part 2
banks_prac = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
import collections

def the_biggest(nums):
    nums = collections.deque([int(x) for x in nums])
    good = []
    count = 0
    while nums:
        x = nums.popleft()
        while good and x > good[-1] and count <88:
            good.pop()
            count+=1

        good.append(x)

    while len(good) > 12:
        good.pop()

    return good


summer2 = 0
for bank in banks:
    good = the_biggest(bank)
    summer2 += int(''.join([str(x) for x in good]))
    


print("The code is: ", summer2)



