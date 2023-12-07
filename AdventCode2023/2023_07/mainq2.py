
from collections import defaultdict

prefix = "AdventCode2023/2023_07/" 

# fileName = "test.txt"
fileName = "input.txt"

fileName = prefix + fileName 

data = defaultdict(list)
# ## QUEST 1 
with open(fileName) as file:
    line = file.readline()
    while line:
        data[line.split()[0]].append(line.split()[1])
        line = file.readline()

L = len(data)
# maxL = 0
# for a in data.values():
#     maxL = max(maxL,len(a))

fiveKind = defaultdict(list)
fourKind = defaultdict(list)
fullKind = defaultdict(list)
threeKind = defaultdict(list)
twoPairKind = defaultdict(list)
onePairKind = defaultdict(list)
highCardKind = defaultdict(list)

listSymb = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]


for a in data.keys():
    maxNbSymb = 0
    s=""
    for symb in listSymb:
        if a.count(symb)>maxNbSymb:
            maxNbSymb = max(maxNbSymb,a.count(symb))
            s = symb
        elif a.count(symb)==maxNbSymb and s=="J":
            s = symb

    if s == "J":
        if maxNbSymb==5 or maxNbSymb==4:
            fiveKind[a].append(data[a])
        elif maxNbSymb==3:
            l = a.replace("J","")
            assert len(l)==2
            if l[0]==l[1]:
                fiveKind[a].append(data[a])
            else:
                fourKind[a].append(data[a])
        elif maxNbSymb==2:
            l = a.replace("J","")
            co = 0
            for symb in listSymb:
                co = max(co,l.count(symb))
            assert co<=2
            if co==2:
                fourKind[a].append(data[a])
            else:
                threeKind[a].append(data[a])
    else:
        if maxNbSymb==5:
            fiveKind[a].append(data[a])
        elif maxNbSymb==4:
            l = a.replace(s,"")
            assert len(l)==1
            if l=="J":
                fiveKind[a].append(data[a])
            else:
                fourKind[a].append(data[a])

        elif maxNbSymb==3:
            l = a.replace(s,"")
            assert len(l)==2
            if (l[0]=="J" and l[1]=="J"):
                fiveKind[a].append(data[a])
            elif (l[0]=="J" or l[1]=="J"):
                fourKind[a].append(data[a])
            else:
                if l[0]==l[1]:
                    fullKind[a].append(data[a])
                else:
                    threeKind[a].append(data[a])
        elif maxNbSymb==2:
            l = a.replace(s,"")
            assert len(l)==3
            maxJ = l.count("J")
            if maxJ==2:
                fourKind[a].append(data[a])
            elif maxJ==1:
                y = l.replace("J","")
                assert len(y)==2
                if y[0]==y[1]:
                    fullKind[a].append(data[a])
                else:
                    threeKind[a].append(data[a])
            else:
                co = 0
                for symb in listSymb:
                    co = max(co,l.count(symb))
                assert co<=2
                if co==2:
                    twoPairKind[a].append(data[a])
                else:
                    onePairKind[a].append(data[a])
        else:
            if a.count("J")==1:
                onePairKind[a].append(data[a])
            else:
                highCardKind[a].append(data[a])

i = 0
ans = 0

def sortKey(a):
    res = 0
    for c in a:
        c = c.replace("T","10").replace("J","1").replace("Q","12").replace("K","13").replace("A","14")
        res += res*1000 + int(c)
    return res

newL = [c for c in fiveKind.keys()]
newL.sort(key=sortKey,reverse=True)
for b in newL:
    ans += (L-i)*sum([int(h) for h in data[b]])
    i += 1

newL = [c for c in fourKind.keys()]
newL.sort(key=sortKey,reverse=True)
for b in newL:
    ans += (L-i)*sum([int(h) for h in data[b]])
    i += 1

newL = [c for c in fullKind.keys()]
newL.sort(key=sortKey,reverse=True)
for b in newL:
    ans += (L-i)*sum([int(h) for h in data[b]])
    i += 1

newL = [c for c in threeKind.keys()]
newL.sort(key=sortKey,reverse=True)
for b in newL:
    ans += (L-i)*sum([int(h) for h in data[b]])
    i += 1

newL = [c for c in twoPairKind.keys()]
newL.sort(key=sortKey,reverse=True)
for b in newL:
    ans += (L-i)*sum([int(h) for h in data[b]])
    i += 1

newL = [c for c in onePairKind.keys()]
newL.sort(key=sortKey,reverse=True)
for b in newL:
    ans += (L-i)*sum([int(h) for h in data[b]])
    i += 1

newL = [c for c in highCardKind.keys()]
newL.sort(key=sortKey,reverse=True)
for b in newL:
    ans += (L-i)*sum([int(h) for h in data[b]])
    i += 1

print(i)
print(ans)
