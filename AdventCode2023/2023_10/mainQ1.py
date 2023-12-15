import sys
sys.setrecursionlimit(int(1e6))

prefix = "AdventCode2023/2023_10/" 

# fileName = "test.txt"
# fileName = "test2.txt"
fileName = "input.txt"

fileName = prefix + fileName 

with open(fileName) as file:
    data = file.readlines()
map = []
for iLine,line in enumerate(data):
    line = line.strip("\n")
    map.append([x for x in line])
    if "S" in line:
        startPos = (iLine,line.index("S"))
# print(startPos)


def addStep(currentPos : tuple,comingFromPos : tuple, counter : int):
    counter += 1
    match map[currentPos[0]][currentPos[1]]:
        case "|":
            if (currentPos[0]-1,currentPos[1])==comingFromPos:
                addStep((currentPos[0]+1,currentPos[1]),currentPos,counter)
            else:
                addStep((currentPos[0]-1,currentPos[1]),currentPos,counter)
        case "F":
            if (currentPos[0]+1,currentPos[1])==comingFromPos:
                addStep((currentPos[0],currentPos[1]+1),currentPos,counter)
            else:
                addStep((currentPos[0]+1,currentPos[1]),currentPos,counter)      
        case "J":
            if (currentPos[0]-1,currentPos[1])==comingFromPos:
                addStep((currentPos[0],currentPos[1]-1),currentPos,counter)
            else:
                addStep((currentPos[0]-1,currentPos[1]),currentPos,counter) 
        case "7":
            if (currentPos[0]+1,currentPos[1])==comingFromPos:
                addStep((currentPos[0],currentPos[1]-1),currentPos,counter)
            else:
                addStep((currentPos[0]+1,currentPos[1]),currentPos,counter) 
        case "L":
            if (currentPos[0]-1,currentPos[1])==comingFromPos:
                addStep((currentPos[0],currentPos[1]+1),currentPos,counter)
            else:
                addStep((currentPos[0]-1,currentPos[1]),currentPos,counter) 
        case "-":
            if (currentPos[0],currentPos[1]-1)==comingFromPos:
                addStep((currentPos[0],currentPos[1]+1),currentPos,counter)
            else:
                addStep((currentPos[0],currentPos[1]-1),currentPos,counter)
        case "S":
            print("Number of step :")
            print(counter)
            print(counter//2)
        case _:
            print("Error")
            print(currentPos)
            print(map[currentPos[0]][currentPos[1]])

addStep((startPos[0],startPos[1]+1),startPos,1)

