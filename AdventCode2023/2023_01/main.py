prefix = "AdventCode2023/2023_01/" 

# fileName = "test.txt"
# fileName = "test2.txt"
fileName = "input.txt"

fileName = prefix + fileName 

sum = 0
## QUESTION 1 

# with open(fileName) as file:
#     line = file.readline().strip("\n")
#     while line:
#         for char in line:
#             if char.isdigit():
#                 first = char
#                 break

#         for char in line[::-1]:
#             if char.isdigit():
#                 last = char
#                 break 
        
#         sum += int(first+last)

#         line = file.readline().strip("\n")        

listValid = "one, two, three, four, five, six, seven, eight, nine".split(", ")


# with open(fileName) as file:
#     line = file.readline().strip("\n")
#     while line:
#         first = None
#         last = None
#         for i in range(0,len(line),1):
#             if not first:
#                 if line[i].isdigit():
#                     first = line[i]
#             if not last:
#                 if line[-1-i].isdigit():
#                     last = line[-1-i]

#             for j in range(3,6):
#                 if not first:
#                     if line[i:i+j] in listValid:
#                         first = listValid.index(line[i:i+j])+1

#                 if not last:
#                     if line[len(line)-i-j:len(line)-i] in listValid:
#                         last = listValid.index(line[len(line)-i-j:len(line)-i])+1
                        
#             if first and last:
#                 break

#         print(str(first)+str(last))
#         sum += int(str(first)+str(last))

#         line = file.readline().strip("\n")        

with open(fileName) as file:
    data = file.read().strip()
    for line in data.split("\n"):
        digit = []
        for i,c in enumerate(line):
            if c.isdigit():
                digit.append(c)
            for j,d in enumerate(listValid):
                if line[i:].startswith(d):
                    digit.append(str(j+1))

        sum += int(digit[0]+digit[-1])

print(f"Sum is {sum}")