prefix = "AdventCode2023/2023_08/" 

# fileName = "test.txt"
# fileName = "test2.txt"
fileName = "input.txt"

fileName = prefix + fileName 

with open(fileName) as file:
    data = file.readlines()