'''
Day 11
'''

with open("input11") as f:
    pathsfile = f.readlines()

import collections

paths = collections.defaultdict(list)

for i in range(len(pathsfile)):
    paths[pathsfile[i][:3]] = pathsfile[i][5:-1].split(" ")
    
#Part 1
countend = 0

def dfs(node):
    global countend

    for x in paths[node]:
        if x == 'out':
            countend+=1
            return
        else:
            dfs(x)

dfs('you')

print('The number of paths is:', countend)


#Part 2

from functools import cache

@cache
def dfs2(node, fgood, dgood):

    if dgood and not fgood:
        return 0

    total = 0
    for x in paths[node]:
        if x == 'out':
            if dgood and fgood:
                total+=1
                
        else:
            nfgood = fgood or (x == 'fft')
            ndgood = dgood or (x == 'dac')
            total += dfs2(x, nfgood, ndgood)

    return total

dfs2('svr', False, False)