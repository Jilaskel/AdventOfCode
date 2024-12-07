from collections import defaultdict
import copy

prefix = "AdventCode2024/2024_06/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

lines = defaultdict(set)
col = defaultdict(set)
ans = 0
walls = set()
with open(fileName) as file:
    # data = file.read().strip()
    data = file.readlines()
    Xmax = len(data)
    Ymax = len(data[0].strip())
    for x,line in enumerate(data):
        for y,c in enumerate(line):
            if c=="#":
                lines[x].add(y)
                col[y].add(x)
                walls.add((x,y))
            elif c=="^":
                startPos = (x,y)

# currentPos = startPos
# lastDir = 0 
# notFinished = True     
# seen = set()
# while notFinished:
#     x,y = currentPos[0],currentPos[1]
#     minD = Xmax + Ymax
#     nextPos = currentPos
#     if lastDir==0: ## go up 
#         nextPos = (-1,y)
#         for wall in col[y]:
#             if 0<x-wall<minD:
#                 nextPos = (wall+1,y)
#                 minD = x-wall
#         for i in range(nextPos[0],x+1):
#             seen.add((i,y))

#     elif lastDir==2: ## go down 
#         nextPos = (Xmax,y)
#         for wall in col[y]:
#             if 0<wall-x<minD:
#                 nextPos = (wall-1,y)
#                 minD = wall - x 

#         for i in range(x,nextPos[0]+1):
#             seen.add((i,y))

#     elif lastDir==1: ## go right 
#         nextPos = (x,Ymax)
#         for wall in lines[x]:
#             if 0<wall-y<minD:
#                 nextPos = (x,wall-1)
#                 minD = wall-y

#         for i in range(y,nextPos[1]+1):
#             seen.add((x,i))

#     elif lastDir==3: ## go left
#         nextPos = (x,-1) 
#         for wall in lines[x]:
#             if 0<y-wall<minD:
#                 nextPos = (x,wall+1)
#                 minD = y-wall

#         for i in range(nextPos[1],y+1):
#             seen.add((x,i))

#     if not(-1<nextPos[0]<Xmax and -1<nextPos[1]<Ymax):
#         notFinished = False
#     else:
#         currentPos = nextPos
#         lastDir = (lastDir +1)%4
    
#     # for i in range(Xmax):
#     #     mystr = ""
#     #     for j in range(Ymax):
#     #         if (i,j) in seen:
#     #             mystr += "X"
#     #         elif (i,j) in walls:
#     #             mystr += "#"
#     #         else:
#     #             mystr += "."
#     #     print(mystr)
#     # print(" ")
#     # print(" ")
 
# ans = len(seen) - 1 ## last step is outside
# print(ans)

## QUEST 2 

maxSameSeen = 4

## pour optimiser, il suffisait de parcourir les positions contenus dans le précédent seen, car sinon le garde ne touchera juste pas l'obstacle...
## pour déterminer si le garde est bloqué dans une boucle, il suffit de stocké un tuple avec sa position ET son orientation 

for xi in range(Xmax):
    print("Beginning line " + str(xi) + "/" + str(Xmax))
    for yi in range(Ymax):

        if (xi,yi)==startPos or (xi,yi) in walls:
            continue

        newCol = copy.deepcopy(col)   ## sinon les dico de base col et line était modifié....
        newCol[yi].add(xi)
        newLines = copy.deepcopy(lines)
        newLines[xi].add(yi)

        sameSeen = 0
        lastSeen = 0

        currentPos = startPos
        lastDir = 0 
        notFinished = True     
        seen = set()
        while notFinished:
            x,y = currentPos[0],currentPos[1]
            minD = Xmax + Ymax
            nextPos = currentPos

            if lastDir==0: ## go up 
                nextPos = (-1,y)
                for wall in newCol[y]:
                    if 0<x-wall<minD:
                        nextPos = (wall+1,y)
                        minD = x-wall
                for i in range(nextPos[0],x+1):
                    seen.add((i,y))

            elif lastDir==2: ## go down 
                nextPos = (Xmax,y)
                for wall in newCol[y]:
                    if 0<wall-x<minD:
                        nextPos = (wall-1,y)
                        minD = wall-x 
                for i in range(x,nextPos[0]+1):
                    seen.add((i,y))

            elif lastDir==1: ## go right 
                nextPos = (x,Ymax)
                for wall in newLines[x]:
                    if 0<wall-y<minD:
                        nextPos = (x,wall-1)
                        minD = wall-y
                for i in range(y,nextPos[1]+1):
                    seen.add((x,i))

            elif lastDir==3: ## go left
                nextPos = (x,-1) 
                for wall in newLines[x]:
                    if 0<y-wall<minD:
                        nextPos = (x,wall+1)
                        minD = y-wall
                for i in range(nextPos[1],y+1):
                    seen.add((x,i))

            if not(-1<nextPos[0]<Xmax and -1<nextPos[1]<Ymax):
                notFinished = False
            else:
                currentPos = nextPos
                lastDir = (lastDir +1)%4

            if(len(seen)==lastSeen):
                sameSeen += 1
                if sameSeen==maxSameSeen:
                    ans += 1
                    # print(xi,yi)
                    notFinished = False
            else:
                lastSeen = len(seen)
                sameSeen = 0
            
            # for i in range(Xmax):
            #     mystr = ""
            #     for j in range(Ymax):
            #         if (i,j) in seen:
            #             mystr += "X"
            #         elif (i,j) in walls:
            #             mystr += "#"
            #         else:
            #             mystr += "."
            #     print(mystr)
            # print(" ")
            # print(" ")
 
print(ans)