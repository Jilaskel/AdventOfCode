prefix = "AdventCode2024/2024_01/" 

fileName = "test.txt"
# fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

    

with open(fileName) as file:
    data = file.read().strip()
    # data = file.readlines()
    for line in data.split("\n"):
