prefix = "AdventCode2024/2024_03/" 

# fileName = "test2.txt"
fileName = "input.txt"

fileName = prefix + fileName 

## QUESTION 1 

with open(fileName) as file:
    data = file.read().strip()
    ans = 0
    splited = data.split("mul(")
    l = len(splited)
    enable_next = True
for i in range(1,l):
    b = splited[i]
    if enable_next:
        ok = False
        X = ""
        Y = ""
        for j in range(4):
            if (b[j].isdigit() and len(X)<4):
                X += b[j]
            elif (b[j]=="," and 0<len(X)<4):
                ok = True
                break
            else:
                ok = False
                break
        if not ok:
            continue
        ok = False
        for k in range(j+1,j+5):
            if (b[k].isdigit() and len(Y)<4):
                Y += b[k]
            elif (b[k]==")" and 0<len(Y)<4):
                ok = True
                break
            else:
                ok = False
                break
        if ok:
            # print(X+ " x "+Y)
            ans += int(X)*int(Y)

    c = b.split("do")
    if c[-1].startswith("n't()"):
        enable_next = False
    elif c[-1].startswith("()"):
        enable_next = True

print(ans)

## QUESTION 2 

