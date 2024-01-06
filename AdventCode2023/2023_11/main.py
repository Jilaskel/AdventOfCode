import queue

prefix = "AdventCode2023/2023_11/" 

fileName = "test.txt"
# fileName = "test2.txt"
# fileName = "input.txt"

fileName = prefix + fileName 

with open(fileName) as file:
    data = file.readlines()

map = []
nbColum = len(data[0].strip("\n"))
indexGalaxy = set()

for line in data:
    line = line.strip("\n")
    not_empty = False
    newL = []
    for ind,a in enumerate(line):
        if a != ".":
            not_empty = True
            indexGalaxy.add(ind)

        newL.append(a)
    map.append(newL)
    if not not_empty:
        map.append(newL.copy())

colToAdd = list(indexGalaxy.symmetric_difference(set([i for i in range(nbColum)])))
colToAdd.sort(reverse=True)

for line in map:
    for indCol in colToAdd:
        line.insert(indCol,".")

for a in map:
    print(a)

sPos = set()

for iLine,line in enumerate(map):
    for jLine,a in enumerate(line):
        if a=="#":
            sPos.add((iLine,jLine))

print(sPos)
ePos = sPos.copy()

ans = 0

for sp in sPos:
    ePos.remove(sp)

    for ep in ePos:
        ans += abs(sp[0]-ep[0]) + abs(sp[1]-ep[1]) 


print(f'ans : {ans}')



