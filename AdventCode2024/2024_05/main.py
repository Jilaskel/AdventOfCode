from collections import defaultdict

prefix = "AdventCode2024/2024_05/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

# rules = defaultdict(list)    
# ans = 0
# with open(fileName) as file:
#     data = file.read().strip()
#     # data = file.readlines()
#     for line in data.split("\n"):
#         if "|" in line:
#             a = int(line[0]+line[1])
#             b = int(line[3]+line[4])
#             rules[a].append((b,1))
#             rules[b].append((a,-1))
#         elif line:
#             update = [int(a) for a in line.split(",")]
#             ok = True
#             for ind,a in enumerate(update):
#                 if a in rules:
#                     for r in rules[a]:
#                         b = r[0]
#                         sign = r[1]
#                         if (b in update[:ind] and sign>0) or (b in update[ind:] and sign<0):
#                             ok = False
#                             break

#                 if not ok:
#                     break

#             if ok:
#                 mid = int(len(update)/2)
#                 ans += update[mid]
# print(ans)


## QUEST 2

rules = defaultdict(list)    
ans = 0
with open(fileName) as file:
    data = file.read().strip()
    # data = file.readlines()
    for line in data.split("\n"):
        if "|" in line:
            a = int(line[0]+line[1])
            b = int(line[3]+line[4])
            rules[a].append((b,1))
            rules[b].append((a,-1))
        elif line:
            update = [int(a) for a in line.split(",")]
            ok = True
            for ind,a in enumerate(update):
                if a in rules:
                    for r in rules[a]:
                        b = r[0]
                        sign = r[1]
                        if (b in update[:ind] and sign>0) or (b in update[ind:] and sign<0):
                            ok = False
                            break

                if not ok:
                    break

            if not ok:
                # le = len(update)
                # pos = defaultdict(int)
                # sup = defaultdict(set)
                # for ind,a in enumerate(update):
                #     if a in rules:
                #         for r in rules[a]:
                #             b = r[0]
                #             sign = r[1]  
                #             if (b in update[ind:]):
                #                 if sign>0:
                #                     sup[b].add(a)
                #                     oldpos = pos[b]
                #                     if pos[b]<=pos[a]:
                #                         pos[b] = pos[a]+1
                #                         delta = pos[b] - oldpos
                #                         for x,y in sup.items():
                #                             if b in y and pos[b]<=pos[x]:
                #                                 pos[x] += delta
                #                 elif sign<0:
                #                     sup[a].add(b)
                #                     oldpos = pos[a]
                #                     if pos[b]>=pos[a]:
                #                         pos[a] = pos[b]+1
                #                         delta = pos[a] - oldpos
                #                         for x,y in sup.items():
                #                             if a in y and pos[a]<=pos[x]:
                #                                 pos[x] += delta

                # once = False
                # for x,y in pos.items():
                #     if y == int(le/2):
                #         ans += x
                #         if not once:
                #             once = True
                #         else:
                #             print("oula")
                #             print(update)
                #             print(le)
                #             print(pos)
                #             break

                le = len(update)
                once = False
                for ind,a in enumerate(update):
                    if a in rules:
                        inf = 0
                        sup = 0
                        for r in rules[a]:
                            b = r[0]
                            sign = r[1]
                            if  (b in update and sign<0):
                                inf+=1
                            elif (b in update and sign>0):
                                sup+=1
                        if (inf==sup) and inf==int(le/2):
                            if once : 
                                print("merde")
                            once = True
                            ans+=a
                            # pas d ebreak car j'y croyais pas
                
print(ans)