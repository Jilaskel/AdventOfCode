prefix = "AdventCode2023/2023_06/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 


## QUEST 1 
# with open(fileName) as file:
#     data = file.read().strip()
#     ans = 1
#     for iLine,line in enumerate(data.split("\n")):
#         if iLine==0:
#             time = line.split(":")[1].split()
#         else:
#             dist = line.split(":")[1].split()

#     ansList = []
#     for i in range(len(time)):
#         ansList.append(0)
#         timemax = int(time[i])
#         for h in range(1,timemax):
#             distMade = (timemax-h)*h
#             if distMade>int(dist[i]):
#                 ansList[i] += 1
#         ans *= ansList[i]
    
#     print(ansList)
#     print(ans)

with open(fileName) as file:
    data = file.read().strip()
    ans = 1
    for iLine,line in enumerate(data.split("\n")):
        if iLine==0:
            t = (line.split(":")[1].split())
        else:
            d = line.split(":")[1].split()
    timemax =""
    distToBeat =""
    for i in range(len(t)):
        timemax += t[i]
        distToBeat += d[i]
    timemax = int(timemax)
    distToBeat = int(distToBeat)
    ans = 0
    for h in range(1,timemax):
        distMade = (timemax-h)*h
        if distMade>distToBeat:
            ans += 1

    print(ans)