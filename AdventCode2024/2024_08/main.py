from collections import defaultdict

prefix = "AdventCode2024/2024_08/" 

# fileName = "test.txt"
# fileName = "test2.txt"
# fileName = "test3.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

ans = 0   

with open(fileName) as file:
    data = file.readlines()
    Xmax = len(data)
    Ymax = len(data[0].strip())
    antennas = defaultdict(list)
    antennas_pos = defaultdict()
    for x,line in enumerate(data):
        for y,c in enumerate(line.strip()):
            if c != ".":
                antennas[c].append((x,y))
                antennas_pos[(str(x)+"_"+str(y))] = c 

antiNodePos = set()
# QUEST 1

# for antenna,pos in antennas.items():
#     if len(pos)>1:
#         for i,p1 in enumerate(pos[:-1]):
#             for p2 in pos[i+1:]:
#                 newX = 2*p2[0] - p1[0]
#                 newY = 2*p2[1] - p1[1]
#                 if (-1<newX<Xmax) and (-1<newY<Ymax):
#                     antiNodePos.add((newX,newY))

#                 newX = 2*p1[0] - p2[0]
#                 newY = 2*p1[1] - p2[1]
#                 if (-1<newX<Xmax) and (-1<newY<Ymax):
#                     antiNodePos.add((newX,newY))

# QUEST 2

for antenna,pos in antennas.items():
    if len(pos)>1:
        for i,p1 in enumerate(pos[:-1]):
            for p2 in pos[i+1:]:
                d = 1
                while True:
                    newX = d*p2[0] - (d-1)*p1[0]
                    newY = d*p2[1] - (d-1)*p1[1]
                    if (-1<newX<Xmax) and (-1<newY<Ymax):
                        antiNodePos.add((newX,newY))
                        d += 1
                    else:
                        break
                d = 1
                while True:
                    newX = d*p1[0] - (d-1)*p2[0]
                    newY = d*p1[1] - (d-1)*p2[1]
                    if (-1<newX<Xmax) and (-1<newY<Ymax):
                        antiNodePos.add((newX,newY))
                        d += 1
                    else:
                        break


ans = len(antiNodePos)
print(ans)

for i in range(Xmax):
    lineStr = ""
    for j in range(Ymax):
        string = str(i) + "_" + str(j)
        if string in antennas_pos:
            lineStr += antennas_pos[string]
        elif (i,j) in antiNodePos:
            lineStr += "#"
        else:
            lineStr += "."
    print(lineStr)


