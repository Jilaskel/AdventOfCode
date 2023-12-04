prefix = "AdventCode2023/2023_04/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 


## QUEST 1 
# with open(fileName) as file:
#     data = file.read().strip()
#     ans = 0
#     for iLine,line in enumerate(data.split("\n")):
#         line = line.split(": ")[1]
#         winning = set([int(a) for a in line.split("|")[0].strip().split(" ") if a!=""])
#         points = 0
#         for b in line.split("|")[1].strip().split(" "):
#             if b!="":
#                 b = int(b.strip())
#                 if b in winning:
#                     if points:
#                         points*=2
#                     else:
#                         points = 1
#         # print(points)
#         ans += points
# print(ans)


## QUEST 2
with open(fileName) as file:
    data = file.read().strip()
    ans = 0
    nbCopies = [1 for i in range(len(data.split("\n")))]
    for iLine,line in enumerate(data.split("\n")):
        line = line.split(": ")[1]
        winning = set([int(a) for a in line.split("|")[0].strip().split()])
        points = 0
        nbWon = 0
        for b in line.split("|")[1].strip().split():
            b = int(b.strip())
            if b in winning:
                nbWon +=1

        for j in range(nbWon):
            nbCopies[iLine+1+j]+=nbCopies[iLine]
            
        # print(points)
        ans += nbCopies[iLine]
print(ans)
