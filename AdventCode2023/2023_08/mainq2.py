from collections import defaultdict
import math 

prefix = "AdventCode2023/2023_08/" 

# fileName = "test3.txt"
fileName = "input.txt"

fileName = prefix + fileName 

with open(fileName) as file:
    data = file.readlines()

inst = data[0].strip("\n")

map = dict()
startPoints = []

for line in data[2:]:
    line = line.strip("\n")
    firstSTr = line.split(" = ")[0].strip()
    secondSTr = line.split(" = (")[1].split(",")[0].strip()
    thirdSTr = line.split(" = (")[1].split(",")[1].strip(")").strip()
    map[firstSTr] = (secondSTr,thirdSTr)
    assert len(firstSTr)==3
    if firstSTr[2]=="A":
        startPoints.append(firstSTr)


currentList = startPoints.copy()
zEndSets = defaultdict(set)

found = False
loopNb = 0
nbInst = len(inst)

maxLoop = 1e8

mod = [0 for i in range(len(currentList))]

stValid = set()

while not found and loopNb<maxLoop:
    buffList = currentList.copy()
    iFloor = loopNb*nbInst
    for j,st in enumerate(buffList):
        current = st
        for i,side in enumerate(inst):
            if side=="L":
                current = map[current][0]
            elif side=="R":
                current = map[current][1]
            else:
                assert False
            if current[2]=="Z":
                here = iFloor+i+1
                for g in zEndSets[j]:
                    if (here-g)%nbInst!=0:
                        assert False
                    else:
                        print("check")
                        stValid.add(j)

                zEndSets[j].add(here)

        currentList[j] = current  ## for next search
    
    if len(zEndSets) == len(currentList):
        found = True
    
    if len(stValid)==len(currentList):
        found=True
    else:
        # zEndSets = defaultdict(set)
        loopNb += 1
    

res = zEndSets[0]
for s in zEndSets.values():
    res = res.union(s)
ans = 1
for a in res:
    ans = math.lcm(ans,a)
print(ans)