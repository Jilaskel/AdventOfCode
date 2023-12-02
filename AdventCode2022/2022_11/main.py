
import time 
import numpy as np

class Item:
    def __init__(self, wLvl : int) -> None:
        self.worryLvl = wLvl
        self.remainder = None
        self.number = None

class Monkey:
    def __init__(self, group, number : int, startingItems : list, op : str, test : int, trueNumber : int, falseNumber : int) -> None:

        self.myGroup = group

        self.number = number

        self.myItems = []
        for wLvl in startingItems:
            thisItem = Item(wLvl)
            self.myItems.append(thisItem)
            self.myGroup.allItems.append(thisItem)

        self.op = op
        match self.op[0]:
            case "m":
                self.factor = int(self.op.split("m")[1])
                self.op = op[0]
            case "a":
                self.factor = int(self.op.split("a")[1])
                self.op = op[0]

        self.test = test
        self.trueNumber = trueNumber
        self.falseNumber = falseNumber

        self.numberOfItemInspected = 0



    def inspect(self, item : Item):
        timeBefore = time.perf_counter()

        match self.op:
            case "m":
                # item.worryLvl *= self.factor
                # item.remainder[:] *= self.factor
                for a in range(len(item.remainder)):
                    f = item.remainder[a]
                    item.remainder[a] = f *self.factor
            case "a":               
                # item.worryLvl += self.factor
                # item.remainder[:] += self.factor
                for a in range(len(item.remainder)):
                    f = item.remainder[a]
                    item.remainder[a] = f + self.factor
            case "s":
                # item.worryLvl = item.worryLvl*item.worryLvl
                for a in range(len(item.remainder)):
                    x = item.remainder[a]
                    item.remainder[a] = int(x * x)
            case _:
                raise Exception("Should not happen!")
            
        self.numberOfItemInspected += 1        

        # item.worryLvl = int(float(item.worryLvl)/3.0)  ## QUESTION 1
        # for a in range(len(item.remainder)):
        #     item.remainder[a] = int(float(item.remainder[a])/3.0)

        dt = time.perf_counter() - timeBefore
        self.myGroup.inspectTime += dt

    def throw(self, item: Item):
        timeBefore = time.perf_counter()

        for a in range(len(item.remainder)):
            buff0 = item.remainder[a]
            buff = buff0%self.myGroup.allDivTest[a]
            item.remainder[a] = int(buff) 

        # buff0 = item.remainder[self.number]
        # buff = buff0%self.test
        # # buff = item.remainder[self.number]%self.test
        # item.remainder[self.number] = int(buff)

        # if self.test != self.myGroup.allDivTest[self.number]:
        #     raise Exception("Issue with indexes")

        # if item.worryLvl%self.test != item.remainder[self.number]:
        #     raise Exception("Explosion !! ")

        if item.remainder[self.number] == 0:
        # if item.worryLvl%self.test == 0:
            self.myGroup.gr[self.trueNumber].myItems.append(item)
        else:
            self.myGroup.gr[self.falseNumber].myItems.append(item)

        self.myItems.pop(0)

        dt = time.perf_counter() - timeBefore
        self.myGroup.throwTime += dt

    def playTurn(self):
        itemToCheck = [item for item in self.myItems]
        for item in itemToCheck:
            self.inspect(item)
            self.throw(item)


class MonkeyGroup():
    def __init__(self) -> None:
        self.gr = []

        self.allItems = []
        self.allDivTest = []

        self.startTime = time.perf_counter()

        self.inspectTime = 0.0
        self.throwTime = 0.0
        self.toto = 0.0
        self.totalTime = 0.0

    def setItems(self):
        h = 0
        for item in self.allItems:
            item.number = h
            # item.remainder = np.zeros(int(len(self.gr)),dtype = int)
            item.remainder = [0 for i in range(len(self.gr))]
            for a in range(len(item.remainder)):
                item.remainder[a] = int(item.worryLvl%self.allDivTest[a])
            h += 1

    def adding(self, monkey : Monkey):
        self.gr.append(monkey)
        monkey.myGroup = self

    def playRound(self):
        for monkey in self.gr:
            monkey.playTurn()


    def playRounds(self, numberRounds : int):
        for i in range(1,numberRounds+1):
            self.playRound()
            if i%100 == 0 or i==20:
                print(f"== After round {i}  ({int(i/numberOfRounds*100)} %) ==")
                self.result()

        self.result(final=True)

    def result(self,final = False):
        res = []
        # for monkey in self.gr:
        #     print(f"Monkey {monkey.number} : {[item.worryLvl for item in monkey.myItems]} ")

        for monkey in self.gr:
            res.append(monkey.numberOfItemInspected)
            print(f"Monkey {monkey.number} inspected items {monkey.numberOfItemInspected} times.")

        self.totalTime = time.perf_counter() - self.startTime
        print(f" Total time : {round(self.totalTime,2)} s")
        print(f" Time to inspect {round(self.inspectTime/self.totalTime,2)*100} %")
        print(f" Time to throw {round(self.throwTime/self.totalTime,2)*100} %")
        print(f" Time to toto {round(self.toto/self.totalTime,2)*100} %")

        if final :
            res.sort()
            print(f" Monkey business is {res[-1]} x {res[-2]} = {res[-1]*res[-2]}")



monkeyGroup = MonkeyGroup()

# TEST
# monkeyGroup.adding(Monkey(0, [79, 98], "m19", 23, 2, 3))
# monkeyGroup.adding(Monkey(1, [54, 65, 75, 74], "a6", 19, 2, 0))
# monkeyGroup.adding(Monkey(2, [79, 60, 97], "s", 13, 1, 3))
# monkeyGroup.adding(Monkey(3, [74], "a3", 17, 0, 1))

# number : int, startingItems : list, op : str, test : int, trueNumber : int, falseNumber : int

# fileName = "test.txt"
fileName = "input.txt"


with open(fileName) as file:
    line = file.readline().strip("\n")
    while line:
        data = []
        data.append(line)
        for i in range(6):
            line = file.readline().strip("\n")
            data.append(line)

        number = int(data[0].split("Monkey ")[1][0])

        stList = [int(nb) for nb in data[1].split(": ")[1].split(", ")]

        opLine = data[2]
        if "+" in opLine:
            op = "a" + opLine.split("+ ")[1]
        else:
            endLine = opLine.split("* ")[1]
            if "old" in endLine:
                op = "s"
            else:
                op = "m" + endLine

        test = int(data[3].split("divisible by ")[1])
        monkeyGroup.allDivTest.append(test)

        trueNumber = int(data[4][-1])
        falseNumber = int(data[5][-1])

        monkeyGroup.adding(Monkey(monkeyGroup,number,stList, op, test, trueNumber, falseNumber))

        line = file.readline().strip("\n")
        

monkeyGroup.setItems()

# numberOfRounds = 1
# numberOfRounds = 20  # QUESTION 1
numberOfRounds = 10000



monkeyGroup.playRounds(numberOfRounds)
