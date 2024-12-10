from collections import deque

prefix = "AdventCode2024/2024_09/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

# ans = 0
# with open(fileName) as file:
#     data = file.read().strip()
#     # data = file.readlines()
#     newLine = []
#     stack = deque()
#     for i,c in enumerate(data):
#         a = int(c)
#         if i%2 == 0:
#             for j in range (a):
#                 newLine.append(str(int(i/2)))
#                 stack.append(int(i/2))
#         else:
#             for j in range(a):
#                 newLine.append(".")
#                 stack.append(-1)
# print(newLine)


# babyLine = []
# for i,c in enumerate(newLine):
#     if len(stack) == i:
#         break
#     if c==".":
#         n = stack.pop()
#         while n == -1:
#             n = stack.pop()
#         babyLine.append(str(n))
#     else:
#         babyLine.append(c)

# print(babyLine)

# for i,c in enumerate(babyLine):
#     ans += i*int(c)

# print(ans)

## QUESTION 2

ans = 0
with open(fileName) as file:
    data = file.read().strip()
    # data = file.readlines()
    newLine = []
    li = deque()
    dot = deque()
    for i,c in enumerate(data):
        a = int(c)
        if i%2 == 0:
            id = len(newLine)
            for j in range (a):
                newLine.append(str(int(i/2)))
            if a>0:
                # nbdigit = len(str(int(i/2)))
                li.appendleft((str(int(i/2)),id,a))
        else:
            id = len(newLine)
            for j in range(a):
                newLine.append(".")
            if (a>0):
                dot.append([id,a])
                # stack.append(-1)
print(newLine)
li = list(li)
babyLine = newLine.copy()

# finalLine = ""
# for c in babyLine:
#     finalLine += str(c)
# print(finalLine)

for nb in li:
    n,id,a = nb
    for d in dot:
        iddot,nbdot = d
        if (nbdot>=a and iddot<id):
            for k in range(a):
                # nbdigit = len(n)
                nbdigit = 1
                babyLine[iddot+k] = n
                newstr = ""
                for g in range(nbdigit):
                    newstr += "."
                babyLine[id+k] = newstr
            d[0] = d[0] + a
            d[1] = d[1] - a
            break
    # finalLine = ""
    # for c in babyLine:
    #     finalLine += str(c)
    # print(finalLine)

# print(babyLine)

# finalLine = ""
# for c in babyLine:
#     finalLine += str(c)
# # print(finalLine)

# for i,c in enumerate(finalLine):
#     if c!=".":
#         ans += i*int(c)

for i,c in enumerate(babyLine):
    if c!=".":
        ans += i*int(c)

print(ans)

