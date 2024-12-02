prefix = "AdventCode2024/2024_01/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

with open(fileName) as file:
    data = file.read().strip()
    # data = file.readlines()
    left = []
    right = []
    for line in data.split("\n"):
        left.append(int(line.split(" ")[0]))
        right.append(int(line.split(" ")[-1]))
left.sort()
right.sort()

sum = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])

print("Question 1 : " + str(sum)) 

sum2 = 0

for a in left:
    sum2+= right.count(a)*a


print("Question 2 : " + str(sum2)) 