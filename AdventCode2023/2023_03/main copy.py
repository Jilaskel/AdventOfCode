from collections import defaultdict

prefix = "AdventCode2023/2023_03/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

map = []

with open(fileName) as file:
    data = file.read().strip()
    for iLine, line in enumerate(data.split("\n")):
        map.append([c for c in line])

xDim = len(map[0])
yDim = len(map)

gearPos = set()
gearDic = defaultdict(list)

def lookAround(map,i,j,gearPos) -> bool:
    for a in [-1,0,1]: 
        for b in [-1,0,1]:
            if 0<=i+a<xDim and 0<=j+b<yDim:
                res = look(map,i+a,j+b,gearPos)
                if res:
                    return True
    return False

def look(map,i,j,gearPos) -> bool:
    res = map[i][j]
    if not(res.isdigit()) and not(res=="."):
        if res=="*":
            gearPos.add((i,j))
        return True


ans1 = 0

for iLine,line in enumerate(map):
    found = ""
    col = None
    valid = False
    for jLine,c in enumerate(line):
        if c.isdigit():
            test = lookAround(map,iLine,jLine,gearPos)
            if test:
                valid = test
            found += c
        else:
            if found != "":
                if valid:
                    ans1 += int(found)
                    for pos in gearPos:
                        gearDic[str(pos)].append(int(found))
                gearPos = set()
                found=""
                valid=False                   
    if found !="":
        if valid:
            ans1 += int(found)
        found=""
        valid=False    

ans2 = 0
for key in gearDic.keys():
    if len(gearDic[key])==2:
        ans2 += gearDic[key][0] * gearDic[key][1]  

print(ans1)
print(ans2)


            

