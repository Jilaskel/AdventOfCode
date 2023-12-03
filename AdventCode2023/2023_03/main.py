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

allFound = dict()

for iLine,line in enumerate(map):
    found = ""
    col = None
    for jLine,c in enumerate(line):
        if c.isdigit():
            found += c
            if not col:
                col = jLine
        else:
            if found != "":
                allFound[str(iLine)+" "+str(col)]=found
                found=""
                col = None
    if found !="":
        allFound[str(iLine)+" "+str(col)]=found
        found=""
        col = None   

gearPos = set()

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
    
def checkGear(map,i,j):
    res = []
    for a in [-1,0,1]: 
        for b in [-1,0,1]:
            if 0<=i+a<xDim and 0<=j+b<yDim:
                if map[i+a][j+b].isdigit():
                    res.append(map[i+a][j+b])

validList = []
for key,value in allFound.items():
    loc = (int(key.split(" ")[0]),int(key.split(" ")[1]))
    length = len(value)
    for j in range(loc[1],loc[1]+length):
        valid = lookAround(map,loc[0],j,gearPos)
        if valid:
            validList.append(value)
            break
        
print(f" found one more number valid, dk why : {len(validList)}")

print(sum([int(a) for a in validList]))

            

