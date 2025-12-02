'''
DAY 2
'''


with open("input2") as file:
    ranges = file.read()


ranges = ranges.split(',')

for i in range(len(ranges)):
    ranges[i] = ranges[i].split('-')




ranges_prac = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
ranges_prac = ranges_prac.split(',')
for i in range(len(ranges_prac)):
    ranges_prac[i] = ranges_prac[i].split('-')

#part 1

def invalid(num):
    n = len(num)
    if n %2 != 0:
        return False
    
    if num.endswith(num[:(n//2)]):
        return True
    else:
        return False
    




invalids = []
#iterate through
adding = 0
for x,y in ranges:
    for i in range(int(x), int(y)+1):
        if invalid(str(i)):
            invalids.append(i)
            adding += i

sum(invalids)
adding


#Part 2
def invalid(num):
    n = len(num)
    for i in range(n//2):
        if n %(i+1) == 0:
            rest = n//(i+1)

        else:
            continue
        if num.endswith(num[:i+1] * rest):
            return True
    return False



invalids = []
#iterate through
adding = 0
for x,y in ranges:
    for i in range(int(x), int(y)+1):
        if invalid(str(i)):
            invalids.append(i)
            adding += i

sum(invalids)
adding