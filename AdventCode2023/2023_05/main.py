import queue
prefix = "AdventCode2023/2023_05/" 

# fileName = "test.txt"
fileName = "input.txt"

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
    data.append("\n")  ## for last
    ans = 0
    j = 0
    ### QUESTION 2
    seeds = queue.Queue()
    for indA,a in enumerate(data[0].split(": ")[1].strip("\n").split()):
        if indA%2==0:
            begin = int(a)
        else:
            seeds.put((begin,begin+int(a)))

    for iLine,line in enumerate(data[2:]):
        if ":" in line:
            B = []
            
        elif (line=="\n"):
            new_s = queue.Queue()
            while not(seeds.empty()):
                (s,sEnd) = seeds.get()
                found = False
                for A in B:
                    if A[1]<=s<=A[1]+A[2]:
                        dh = s - A[1]
                        h = A[0] + dh
                        newS = h
                        if sEnd<=A[1]+A[2]:
                            dh = sEnd - A[1]
                            h = A[0] + dh
                            newSEnd = h
                            new_s.put((newS,newSEnd))
                        else:
                            new_s.put((newS,A[0]+A[2]))
                            seeds.put((A[1]+A[2]+1,sEnd))
                        found = True
                        break
                    elif A[1]<=sEnd<=A[1]+A[2]:
                        # raise Exception("Merde")
                        dh = sEnd - A[1]
                        h = A[0] + dh
                        newSend = h
                        new_s.put((A[0],newSend))
                        seeds.put((s,A[1]-1))
                        found = True
                        break
                if not found:
                    new_s.put((s,sEnd))
                    
            seeds = new_s
        else:
            line = line.strip("\n")
            B.append([int(b) for b in line.split()])
            ind = 0
        


final = []
while not(seeds.empty()):
    s=seeds.get()
    # print(s)
    final.append(s[0])
# print(seeds)
ans = min(final)
print(ans)