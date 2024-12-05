prefix = "AdventCode2024/2024_04/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

    

with open(fileName) as file:
    # data = file.readlines()
    datas = file.read().strip()
    data = datas.split("\n")
    # print(data)
ans = 0
# for i,line in enumerate(data):
#     l = list(line)
#     X = int(len(l))
#     # for j,c in enumerate(l):
#     for j in range(X):
#         Y = len(data[i])
#         c = data[i][j]
#         if c=="X":
#             if (j-3>-1):
#                 if data[i][j-1]+data[i][j-2]+data[i][j-3] == "MAS":
#                     ans +=1
#                     print (i,j, "gauche")
#             if (j+3<Y):
#                 if data[i][j+1]+data[i][j+2]+data[i][j+3] == "MAS":
#                     ans +=1
#                     print (i,j, "droite")

#             if (i-3>-1):
#                 if data[i-1][j]+data[i-2][j]+data[i-3][j] == "MAS":
#                     ans +=1
#                     print (i,j, "haut")

#             if (i+3<X):
#                 if data[i+1][j]+data[i+2][j]+data[i+3][j] == "MAS":
#                     ans +=1
#                     print (i,j, "bas")

#             if (i-3>-1 and j-3>-1):
#                 if data[i-1][j-1]+data[i-2][j-2]+data[i-3][j-3] == "MAS":
#                     ans +=1
#                     print (i,j, "diag hg")

#             if (i-3>-1 and j+3<Y):
#                 if data[i-1][j+1]+data[i-2][j+2]+data[i-3][j+3] == "MAS":
#                     ans +=1
#                     print (i,j, "diag hd")

#             if (i+3<X and j-3>-1):
#                 if data[i+1][j-1]+data[i+2][j-2]+data[i+3][j-3] == "MAS":
#                     ans +=1
#                     print (i,j, "diag bg")

#             if (i+3<X and j+3<Y):
#                 if data[i+1][j+1]+data[i+2][j+2]+data[i+3][j+3] == "MAS":
#                     ans +=1
#                     print (i,j, "diag bd")


## QUESTION 2

ans = 0
valid = ["M","S"]
for i,line in enumerate(data):
    l = list(line)
    X = int(len(l))
    # for j,c in enumerate(l):
    for j in range(X):
        Y = len(data[i])
        c = data[i][j]
        if c=="A":
            if (X-1>i>0) and (Y-1>j>0):
                hg = data[i-1][j-1]
                bg = data[i+1][j-1]
                hd = data[i-1][j+1]
                bd = data[i+1][j+1]

                if ((hg in valid) and (bd in valid) and (hg != bd)) and ((hd in valid) and (bg in valid) and (hd != bg)):
                    ans += 1

print(ans)