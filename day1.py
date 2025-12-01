'''
DAY ONE
'''


with open("input") as f:
    lines = f.read()



lines = lines.split("\n")

#part one
def circle(num):
    if num >= 100:
        leftover = num - 100
        return 0 + leftover
    elif num < 0:
        leftover = abs(num)
        return 100 - leftover
    return num



curr = 50
count = 0
last = 50
for x in lines:
    if x == "":
        continue
    if x[0] == 'L':
        spin = int(x[1:])%100
        curr -= spin
        curr = circle(curr)
    elif x[0] == "R":
        spin = int(x[1:])%100
        curr += spin
        curr = circle(curr)
    else:
        continue
    if curr == 0:
        count += 1

print(count)

#part 2

count = 0
curr = 50
def circle(num):
    if num >= 100:
        leftover = num - 100
        return 0 + leftover
    elif num < 0:
        leftover = abs(num)
        return 100 - leftover
    return num

for x in lines:
    last = curr
    direction = x[0]
    clicks = int(x[1:])
    count += (clicks // 100)

    if direction == "R":
        spin = clicks%100
        curr += spin
        if last + spin > 100:
            count+=1
        curr = circle(curr)

    if direction == "L":
        spin = clicks%100
        curr -= spin
        if spin>last and last !=0:
            count += 1
        curr = circle(curr)

    if curr == 0:
        count +=1

print(count)






