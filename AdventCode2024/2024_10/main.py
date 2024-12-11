import queue

prefix = "AdventCode2024/2024_10/" 

# fileName = "test.txt"
fileName = "test2.txt"
# fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

startPos = set()

with open(fileName) as file:
    data = file.read().strip()
    # data = file.readlines()
    map = data.split("\n")
    for x,line in enumerate(map):
        for y,c in enumerate(line.strip()):
            if int(c)==0:
                startPos.add((x,y))

maxX = len(map)
maxY = len(map[0])

DIR = [0 ,1, 0, -1, 0]
def getNeigh(x : int, y : int):
    out = set()
    v = int(map[x][y])
    for i in range(4):
        nX = x + DIR[i]
        nY = y + DIR[i+1]
        if (-1<nX<maxX and -1<nY<maxY):
            if (int(map[nX][nY])==v+1):
                out.add((nX,nY))
    return out
ans = 0

for sp in startPos:
    frontier = queue.Queue()
    # map = dict()
    frontier.put(sp)
    seen = set()
    while not(frontier.empty()):
        cX, cY = frontier.get()
        if int(map[cX][cY]) == 9:
            ## QUESTION 1
            # if (not((cX,cY) in seen)):
            #    seen.add((cX,cY))
            #    ans += 1
            ## QUESTION 2
            ans += 1
        else:
            for neigh in getNeigh(cX, cY):
                frontier.put(neigh)

print(ans)