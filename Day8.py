'''
Day 8
'''
import numpy as np
import heapq

with open("input8") as f:
    coords = f.readlines()

len(coords)

coords[0]

for i in range(len(coords)):
    coords[i] = coords[i][:-1]

for i in range(len(coords)):
    coords[i] = coords[i].split(',')

for i in range(len(coords)):
    coords[i] = [int(x) for x in coords[i]]

def eucdist(coord1, coord2):
    x1,y1,z1 = coord1
    x2,y2,z2 = coord2

    return np.sqrt(((x1-x2)**2) + ((y1-y2)**2) + ((z1-z2)**2))



#Part 1

mat = np.zeros((1000, 1000))

min_heap = []

for i in range(1000):
    for j in range(1000):
        if mat[j,i] != 0:
            continue
        elif i==j:
            continue
        else:
            euc = eucdist(coords[i],coords[j])
            mat[i][j] += euc
            heapq.heappush(min_heap, [euc, i, j])

conns = []


seen = set()
for _ in range(1000):
    e, x, y = heapq.heappop(min_heap)
    if conns:
        inthere = False
        for i in range(len(conns)):
            if x in conns[i]:
                inthere = True
                if y in seen:
                    if y not in conns[i]:
                        j = i
                        while y not in conns[j]:
                            j+=1
                        conns[i] |= conns[j]
                        conns[j] = set()
                        break
                    else:
                        break
                else:
                    conns[i].add(y)
                    break
            
            elif y in conns[i]:
                inthere = True
                if x in seen:
                    if x not in conns[i]:
                        j = i
                        while x not in conns[j]:
                            j +=1 
                        conns[i] |= conns[j]
                        conns[j] = set()
                        break
                    else:
                        break
                else:
                    conns[i].add(x)
                    break
            
        if not inthere:
            conns.append(set([x,y]))
     
    else:
        conns.append(set([x, y]))
    seen.add(x)
    seen.add(y)




len_conns = []
for x in conns:
    len_conns.append(len(x))

len_conns.sort(reverse=True)


print("Answer: ", np.prod(len_conns[:3]))


#Part 2

mat = np.zeros((1000, 1000))

min_heap = []

for i in range(1000):
    for j in range(1000):
        if mat[j,i] != 0:
            continue
        elif i==j:
            continue
        else:
            euc = eucdist(coords[i],coords[j])
            mat[i][j] += euc
            heapq.heappush(min_heap, [euc, i, j])

conns = [np.nan, np.nan]

seen = set()
while len(conns)>1 or len(conns[0])<1000:
    conns = [x for x in conns if x is not np.nan]
    e, x, y = heapq.heappop(min_heap)
    if conns:
        inthere = False
        for i in range(len(conns)):
            if x in conns[i]:
                inthere = True
                if y in seen:
                    if y not in conns[i]:
                        j = i
                        while y not in conns[j]:
                            j+=1
                        conns[i] |= conns[j]
                        conns[j] = np.nan
                        break
                    else:
                        break
                else:
                    conns[i].add(y)
                    break
            
            elif y in conns[i]:
                inthere = True
                if x in seen:
                    if x not in conns[i]:
                        j = i
                        while x not in conns[j]:
                            j +=1 
                        conns[i] |= conns[j]
                        conns[j] = np.nan
                        break
                    else:
                        break
                else:
                    conns[i].add(x)
                    break
            
        if not inthere:
            conns.append(set([x,y]))
     
    else:
        conns.append(set([x, y]))
    seen.add(x)
    seen.add(y)


print("Answer is: ", coords[x][0] * coords[y][0])





