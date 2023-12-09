prefix = "AdventCode2023/2023_08/" 

# fileName = "test.txt"
# fileName = "test2.txt"
fileName = "input.txt"

fileName = prefix + fileName 

with open(fileName) as file:
    data = file.readlines()

inst = data[0].strip("\n")

map = dict()

for line in data[2:]:
    line = line.strip("\n")
    firstSTr = line.split(" = ")[0].strip()
    secondSTr = line.split(" = (")[1].split(",")[0].strip()
    thirdSTr = line.split(" = (")[1].split(",")[1].strip(")").strip()
    map[firstSTr] = (secondSTr,thirdSTr)

# start = data[2].split(" = ")[0]
start = "AAA"
current = start
i = 0
found = False
while not found:
    for side in inst:
        if side=="L":
            current = map[current][0]
        elif side=="R":
            current = map[current][1]
        else:
            assert False
        i += 1
        if current=="ZZZ":
            found = True
            break
print(i)
