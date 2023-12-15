prefix = "AdventCode2023/2023_09/" 

# fileName = "test.txt"
# fileName = "test2.txt"
fileName = "input.txt"

fileName = prefix + fileName 

with open(fileName) as file:
    data = file.readlines()

## QUESTION 1 
ans = 0
for line in data:
    line = line.strip("\n")
    line = line.split()
    ansLine = int(line[-1])
    not_finished = True
    while (not_finished):
        newLine = []
        not_finished = False
        for i in range(len(line)-1):
            a = int(line[i+1])-int(line[i])
            newLine.append(a)
            if a != 0:
                not_finished = True
        ansLine += newLine[-1]
        line = newLine
    ans += ansLine
print(ans)

## QUESTION 2
ans = 0
for line in data:
    line = line.strip("\n")
    line = line.split()
    ansLine = int(line[0])
    coeff = 1
    not_finished = True
    while (not_finished):
        newLine = []
        not_finished = False
        for i in range(len(line)-1):
            a = int(line[i+1])-int(line[i])
            newLine.append(a)
            if a != 0:
                not_finished = True
        ansLine -= newLine[0]*coeff
        coeff *= -1
        line = newLine
    # print(ansLine)
    ans += ansLine
print(ans)