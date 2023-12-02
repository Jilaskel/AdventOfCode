prefix = "AdventCode2023/2023_02/" 

# fileName = "test.txt"
# fileName = "test2.txt"
fileName = "input.txt"

fileName = prefix + fileName 

maxBlue = 14
maxGreen = 13
maxRed = 12

maxAllow = [maxBlue,maxGreen,maxRed]

gameOk = []

## QUESTION 1

# with open(fileName) as file:
#     data = file.read().strip()
#     for iLine, line in enumerate(data.split("\n")):
#         gameAccepted = True
#         for index,color in enumerate([" blue"," green"," red"]):
#             splitColor = line.split(color)
#             nbColor = []
#             for splitSpace in splitColor[:-1:]:
#                 nbColor.append(int(splitSpace.split(" ")[-1]))
#             maxColor = max(nbColor)
#             if maxColor>maxAllow[index]:
#                 gameAccepted = False
#         if gameAccepted:
#             gameOk.append(iLine+1)

# print(sum(gameOk))

gamePower = []

with open(fileName) as file:
    data = file.read().strip()
    for iLine, line in enumerate(data.split("\n")):
        nbColor = [[] for i in range(3)]
        for partLine in line.split(";"):
            gameAccepted = True
            for index,color in enumerate([" blue"," green"," red"]):
                splitColor = line.split(color)
                for splitSpace in splitColor[:-1:]:
                    nbColor[index].append(int(splitSpace.split(" ")[-1]))

        minList = [max(a) for a in nbColor] 
        gamePower.append(minList[0]*minList[1]*minList[2])

# print(gamePower)
print(sum(gamePower))