from collections import deque

prefix = "AdventCode2024/2024_09/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

ans = 0
with open(fileName) as file:
    data = file.read().strip()
    # data = file.readlines()
    newLine = []
    stack = deque()
    for i,c in enumerate(data):
        a = int(c)
        if i%2 == 0:
            for j in range (a):
                newLine.append(str(int(i/2)))
                stack.append(int(i/2))
        else:
            for j in range(a):
                newLine.append(".")
                stack.append(-1)
# print(newLine)

## QUESTION 1

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

## QUESTION 2

babyLine = []
for i,c in enumerate(newLine):
    if len(stack) == i:
        break
    if c==".":
        n = stack.pop()
        while n == -1:
            n = stack.pop()
        babyLine.append(str(n))
    else:
        babyLine.append(c)

# print(babyLine)

for i,c in enumerate(babyLine):
    ans += i*int(c)

print(ans)

