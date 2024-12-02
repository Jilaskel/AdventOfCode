prefix = "AdventCode2024/2024_02/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

# with open(fileName) as file:
#     data = file.read().strip()
#     ans = 0
#     for line in data.split("\n"):
#         report = [int(a) for a in line.split(" ")]
#         validated = True
#         if (report[0]<report[-1]):
#             mult = -1
#         else:
#             mult = 1
#         for i in range(len(report)-1):
#             if (report[i]*mult>report[i+1]*mult) and (abs(report[i]-report[i+1])>0 and abs(report[i]-report[i+1])<4):
#                 continue
#             else:
#                 validated = False
#                 break
#         if validated:
#             ans +=1

# print("Question 1 : "+str(ans))

## QUESTION 2 : Brut force car le reste n'a pas marché 

with open(fileName) as file:
    data = file.read().strip()
    ans = 0
    for line in data.split("\n"):
        report = [int(a) for a in line.split(" ")]
        validated = True
        for i in range(len(report)):
            test = report[:]
            test.pop(i)
            validated = True
            if (test[0]<test[-1]):
                mult = -1
            else:
                mult = 1
            for i in range(len(test)-1):
                if (test[i]*mult>test[i+1]*mult) and (abs(test[i]-test[i+1])>0 and abs(test[i]-test[i+1])<4):
                    continue
                else:
                    validated = False
                    break
            if validated:
                ans +=1
                break


print("Question 2 : "+str(ans))