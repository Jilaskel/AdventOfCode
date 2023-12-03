import string
import queue
import numpy as np

prefix = "AdventCode2022/2022_12/" 

# fileName = "test.txt"
# fileName = "test2.txt"
fileName = "input.txt"

fileName = prefix + fileName 

alphabet = list(string.ascii_lowercase)

map = []

with open(fileName) as file:
    data = file.read().strip()
    for iLine, line in enumerate(data.split("\n")):
        if "S" in line:
            sLoc = (iLine,line.index("S"))
        if "E" in line:
            eLoc = (iLine,line.index("E"))

        map.append([alphabet.index(x) for x in line.lower()])


map[sLoc[0]][sLoc[1]] = alphabet.index("a")
map[eLoc[0]][eLoc[1]] = alphabet.index("z")


class Map:
    def __init__(self,map) -> None:
        self.data = map
        self.comeFrom = dict()

    def getNeigh(self,loc : tuple) -> list():
        res = []
        i = loc[0]
        j = loc[1]

        currentH = self.data[i][j]

        if i>0:
            dh = self.data[i-1][j] - currentH
            if dh<2:
                res.append((i-1,j))
        if i+1<len(self.data):
            dh = self.data[i+1][j] - currentH
            if dh<2:
                res.append((i+1,j))

        if j>0:
            dh = self.data[i][j-1] - currentH
            if dh<2:
                res.append((i,j-1))
        if j+1<len(self.data[0]):
            dh = self.data[i][j+1] - currentH
            if dh<2:
                res.append((i,j+1))

        return res

    def getNeighQ2(self,loc : tuple) -> list():
        res = []
        i = loc[0]
        j = loc[1]

        currentH = self.data[i][j]

        if i>0:
            dh = self.data[i-1][j] - currentH
            if dh>-2:
                res.append((i-1,j))
        if i+1<len(self.data):
            dh = self.data[i+1][j] - currentH
            if dh>-2:
                res.append((i+1,j))

        if j>0:
            dh = self.data[i][j-1] - currentH
            if dh>-2:
                res.append((i,j-1))
        if j+1<len(self.data[0]):
            dh = self.data[i][j+1] - currentH
            if dh>-2:
                res.append((i,j+1))

        return res
    
    def getH(self,loc : tuple) -> int:
        return(self.data[loc[0]][loc[1]])

myMap = Map(map)

frontier = queue.Queue()
frontier.put(sLoc)



myMap.comeFrom[str(sLoc)] = None

while not(frontier.empty()):
    current = frontier.get()
    if current == eLoc:
        break
    for neigh in myMap.getNeigh(current):
        if not(str(neigh) in myMap.comeFrom):
            myMap.comeFrom[str(neigh)] = current
            frontier.put(neigh)

step = 0

while current!=sLoc:
    current = myMap.comeFrom[str(current)]
    step += 1

print(f"Question 1 : {step}")


myMap = Map(map)

frontier = queue.Queue()
frontier.put(eLoc)

myMap.comeFrom[str(eLoc)] = None

while not(frontier.empty()):
    current = frontier.get()
    if myMap.getH(current) == 0:
        break
    for neigh in myMap.getNeighQ2(current):
        if not(str(neigh) in myMap.comeFrom):
            myMap.comeFrom[str(neigh)] = current
            frontier.put(neigh)

step = 0

while current!=eLoc:
    current = myMap.comeFrom[str(current)]
    step += 1

print(f"Question 2 : {step}")