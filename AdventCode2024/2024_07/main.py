prefix = "AdventCode2024/2024_07/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

    
ans = 0
# with open(fileName) as file:
#     # data = file.read().strip()
#     data = file.readlines()
#     for line in data:
#         result = int(line.split(":")[0])
#         l = line.split(":")[1].strip().split(" ")
#         numb = [int(a) for a in l]

#         # print(result)
#         # print(numb)

#         lastResult = set()
#         lastResult.add(numb[0])

#         for i in range(1,len(numb)):
#             newResult = set()
#             for a in lastResult:
#                 newResult.add(a*numb[i])
#                 newResult.add(a+numb[i])
#             lastResult = newResult

#         if result in lastResult:
#             ans += result
# print(ans)

## QUEST 2

with open(fileName) as file:
    # data = file.read().strip()
    data = file.readlines()
    for iLine,line in enumerate(data):
        print("Computing line "+str(iLine)+" / "+str(len(data)))
        result = int(line.split(":")[0])
        l = line.split(":")[1].strip().split(" ")
        numb = [int(a) for a in l]

        lastResult = set()
        lastResult.add(numb[0])

        for i in range(1,len(numb)):
            newResult = set()
            for a in lastResult:
                newResult.add(a*numb[i])
                newResult.add(a+numb[i])
                newResult.add(int(str(a)+str(numb[i])))

            lastResult = newResult

        if result in lastResult:
            ans += result
print(ans)