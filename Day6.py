'''
Day 6
'''

with open("input6") as f:
    problems = f.readlines()

len(problems)

for i in range(len(problems)):
    problems[i] = problems[i][:-1]


#Part 1

problist = []
for j in range(len(problems)):
    i = 0
    problistv1 = []
    while i < len(problems[j]):
        prob = []
        while i < len(problems[j]) and problems[j][i] != ' ':
            prob.append(problems[j][i])
            i+=1
        if prob:
            problistv1.append(prob)
        else:
            i+=1
    problist.append(problistv1)

#list of vertical problems
probvert = []
for i in range(len(problist[0])):
    p = []
    for j in range(len(problist)-1):
        p.append(int(''.join(problist[j][i])))
    p.append(''.join(problist[-1][i]))
    probvert.append(p)


import math

total = 0
for i in range(len(probvert)):
    a,b,c,d,e = probvert[i]
    if e == "*":
        total += math.prod([a,b,c,d])
    else:
        total += sum([a,b,c,d])

print("The total of the answers is: ", total)


#Part 2

problems2 = problems[:]
#str's to list's
for i in range(len(problems)):
    problems2[i] = [x for x in problems2[i]]

#seperate collumns
problist2 = []
for k in range(len(problems2)):
    new_ps = []
    i = 0
    for j in range(len(problems2[k])):
        count = 0
        for x in range(5):
            if problems2[x][j] == " ":
                count +=1
        if count == 5:
            new_ps.append(problems2[k][i:j])
            i = j+1
        if j == len(problems2[k])-1:
            new_ps.append(problems2[k][i:j+1])
    problist2.append(new_ps)

#list per collumn
probvert2 = []
for i in range(len(problist2[0])):
    problistv2 = [[], [], [], []] 
    for j in range(len(problist2)):
        k = 0
        while k < len(problist2[j][i]):
            problistv2[k].append(problist2[j][i][k])
            k+=1
    probvert2.append(problistv2)

#get opertaions
formula = []
for i in range(len(probvert2)):
    save = probvert2[i][0][-1]
    formula.append(save)
    probvert2[i][0] = probvert2[i][0][:-1]


#lits's to int's
for i in range(len(probvert2)):
    for j in range(len(probvert2[i])):
        if probvert2[i][j]:
           probvert2[i][j] =  int(''.join(probvert2[i][j]).strip())
        else:
            probvert2[i] = probvert2[i][:j]
            break

total2 = 0 
for i in range(len(probvert2)):
    if formula[i] == "*":
        total2 += math.prod(probvert2[i])
    else:
        total2 += sum(probvert2[i])
 
print("The Cephalopod total is : ", total2)







