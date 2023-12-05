prefix = "AdventCode2023/2023_05/" 

fileName = "test.txt"
# fileName = "input.txt"

fileName = prefix + fileName 


# ## QUEST 1 
# with open(fileName) as file:
#     data = file.readlines()
#     ans = 0
#     j = 0
#     seeds =  [int(a) for a in data[0].split(": ")[1].strip("\n").split()]  ### QUESTION 1

#     dicList = []
#     for iLine,line in enumerate(data[2:]):
#         if ":" in line:
#             if dicList!=[]:
#                 j += 1
#             dicList.append(dict())
            
#         elif (line=="\n"):
#             new_s = []
#             # print(seeds)
#             for s in seeds:
#                 if str(s) in dicList[j]:
#                     new_s.append(dicList[j][str(s)])
#                 else:
#                     new_s.append(int(s))
#             seeds = new_s
#         else:
#             line = line.strip("\n")
#             B = [int(b) for b in line.split()]
#             ind = 0
#             for s in seeds:
#                 if B[1]<=s<B[1]+B[2]:
#                     dh = s - B[1]
#                     h = B[0] + dh
#                     dicList[j][str(s)] = h


# new_s = []
# # print(seeds)
# for s in seeds:
#     if str(s) in dicList[j]:
#         new_s.append(dicList[j][str(s)])
#     else:
#         new_s.append(int(s))
# seeds = new_s

# # print(seeds)
# ans = min(seeds)
# print(ans)


## QUEST 2
with open(fileName) as file:
    data = file.readlines()
    ans = 0
    j = 0
    ### QUESTION 2
    seeds = []
    for indA,a in enumerate(data[0].split(": ")[1].strip("\n").split()):
        if indA%2==0:
            begin = int(a)
        else:
            seeds.append((begin,begin+int(a)))

    dicList = []
    for iLine,line in enumerate(data[2:]):
        if ":" in line:
            if dicList!=[]:
                j += 1
            dicList.append(dict())
            
        elif (line=="\n"):
            new_s = []
            # print(seeds)
            for (s,sEnd) in seeds:
                if str(s) in dicList[j]:
                    new_s.append(dicList[j][str(s)])
                else:
                    new_s.append(int(s))
                if str(sEnd) in dicList[j]:
                    new_s.append(dicList[j][str(sEnd)])
                else:
                    new_s.append(int(sEnd))
            seeds = new_s
        else:
            line = line.strip("\n")
            B = [int(b) for b in line.split()]
            ind = 0
            
            # while newL!=[]:
            newL = []
            for (s,sEnd) in seeds:
                if B[1]<=s<B[1]+B[2]:
                    dh = s - B[1]
                    h = B[0] + dh
                    dicList[j][str(s)] = h
                if sEnd<B[1]+B[2]:
                    dh = sEnd - B[1]
                    h = B[0] + dh
                    dicList[j][str(sEnd)] = h
                else:
                    newL.append((B[1]+B[2],sEnd))
            seeds.extend(newL)


new_s = []
# print(seeds)
for s in seeds:
    if str(s) in dicList[j]:
        new_s.append(dicList[j][str(s)])
    else:
        new_s.append(int(s))
seeds = new_s

# print(seeds)
ans = min(seeds)
print(ans)