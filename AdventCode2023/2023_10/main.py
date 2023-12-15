import sys
sys.setrecursionlimit(int(1e6))

prefix = "AdventCode2023/2023_10/" 

# fileName = "test6.txt"
# fileName = "test2.txt"
fileName = "input.txt"

fileName = prefix + fileName 
print(fileName)

with open(fileName) as file:
    data = file.readlines()
map = []
for iLine,line in enumerate(data):
    line = line.strip("\n")
    map.append([x for x in line])
    if "S" in line:
        startPos = (iLine,line.index("S"))
# print(startPos)


def addStep(currentPos : tuple,comingFromPos : tuple, counter : int, setLoop, listLoop):
    counter += 1
    setLoop.add(currentPos)
    listLoop.append(currentPos)
    match map[currentPos[0]][currentPos[1]]:
        case "|":
            if (currentPos[0]-1,currentPos[1])==comingFromPos:
                addStep((currentPos[0]+1,currentPos[1]),currentPos,counter,setLoop,listLoop)
            else:
                addStep((currentPos[0]-1,currentPos[1]),currentPos,counter,setLoop,listLoop)
        case "F":
            if (currentPos[0]+1,currentPos[1])==comingFromPos:
                addStep((currentPos[0],currentPos[1]+1),currentPos,counter,setLoop,listLoop)
            else:
                addStep((currentPos[0]+1,currentPos[1]),currentPos,counter,setLoop,listLoop)      
        case "J":
            if (currentPos[0]-1,currentPos[1])==comingFromPos:
                addStep((currentPos[0],currentPos[1]-1),currentPos,counter,setLoop,listLoop)
            else:
                addStep((currentPos[0]-1,currentPos[1]),currentPos,counter,setLoop,listLoop) 
        case "7":
            if (currentPos[0]+1,currentPos[1])==comingFromPos:
                addStep((currentPos[0],currentPos[1]-1),currentPos,counter,setLoop,listLoop)
            else:
                addStep((currentPos[0]+1,currentPos[1]),currentPos,counter,setLoop,listLoop) 
        case "L":
            if (currentPos[0]-1,currentPos[1])==comingFromPos:
                addStep((currentPos[0],currentPos[1]+1),currentPos,counter,setLoop,listLoop)
            else:
                addStep((currentPos[0]-1,currentPos[1]),currentPos,counter,setLoop,listLoop) 
        case "-":
            if (currentPos[0],currentPos[1]-1)==comingFromPos:
                addStep((currentPos[0],currentPos[1]+1),currentPos,counter,setLoop,listLoop)
            else:
                addStep((currentPos[0],currentPos[1]-1),currentPos,counter,setLoop,listLoop)
        case "S":
            print("Number of step :")
            print(counter)
            print(counter//2)
        case _:
            print("Error")
            print(currentPos)
            print(map[currentPos[0]][currentPos[1]])


setLoop = {startPos}
listLoop = [startPos]

addStep((startPos[0],startPos[1]+1),startPos,1,setLoop,listLoop)
# addStep((startPos[0]+1,startPos[1]),startPos,1,setLoop,listLoop)  ## for test 6


def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


A = (0,0)
if A in setLoop:
    raise Exception('A in the loop !! ')
counterTileInLoop = 0
counterTileInLoopLastLine = 0

for x,line in enumerate(map):

    print(f"Line number : {x+1}, number of tile found in loop : {counterTileInLoop-counterTileInLoopLastLine}")
    counterTileInLoopLastLine = counterTileInLoop

    for y,tile in enumerate(line):
        if not((x,y) in setLoop):
            B = (x,y)
            intersectionNumber = 0
            for i in range(len(listLoop)-1):
                C = (listLoop[i][0],listLoop[i][1])
                D = (listLoop[i+1][0],listLoop[i+1][1])
                if intersect(A,B,C,D):
                    intersectionNumber+=1
            if intersectionNumber%2!=0: ## odd
                counterTileInLoop += 1

print(counterTileInLoop)