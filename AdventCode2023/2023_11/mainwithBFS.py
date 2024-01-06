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

dimX = len(map)
dimY = len(map[0])

for a in map:
    print(a)

def getNeigh(current : tuple) -> list[tuple]:
    res = []
    x = current[0]
    y = current[1]
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            if 0<=(x+a)<dimX and 0<=(y+b)<dimY and (a==0 or b==0):
                res.append((x+a,y+b))
    return res



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

    frontier = queue.Queue()
    frontier.put(sp)

    comeFrom = dict()
    comeFrom[str(sp)] = None

    costSoFar = dict()
    costSoFar[str(sp)] = 0

    while not(frontier.empty()):
        current = frontier.get()
        for neigh in getNeigh(current):
            # if (str(neigh) in costSoFar):
            #     if costSoFar[str(current)]+1>=costSoFar[str(neigh)]:
            #         continue
            # else:
            #     frontier.put(neigh)

            # comeFrom[str(neigh)] = current  
            # costSoFar[str(neigh)] = costSoFar[str(current)]+1

            if not(str(neigh) in costSoFar):
                frontier.put(neigh)
                comeFrom[str(neigh)] = current  
                costSoFar[str(neigh)] = costSoFar[str(current)]+1

    for ep in ePos:
        ans += costSoFar[str(ep)]
    #     print(f'ep : {ep}  cost {costSoFar[str(ep)]}')
    # break

print(f'ans : {ans}')



