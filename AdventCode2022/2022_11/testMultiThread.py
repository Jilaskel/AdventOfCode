
import time 
import numpy as np
import threading


class Item:
    def __init__(self, wLvl : int) -> None:
        self.worryLvl = wLvl
        self.remainder = None
        self.number = None

class Monkey(threading.Thread):
    def __init__(self, group, number : int, startingItems : list, op : str, test : int, trueNumber : int, falseNumber : int) -> None:
        threading.Thread.__init__(self)

        self.myGroup = group

        self.monkeyBefore = None
        self.turnFinished = False

        self.number = number
        self.id = number

        self.myItems = []
        self.seenItems = []
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

        self.itemForNextTurn = []
        self.itemForThisTurn = []



    def inspect(self, item : Item):
        timeBefore = time.perf_counter()


        match self.op:
            case "m":
                for a in range(len(item.remainder)):
                    f = item.remainder[a]
                    item.remainder[a] = f *self.factor
            case "a":               
                for a in range(len(item.remainder)):
                    f = item.remainder[a]
                    item.remainder[a] = f + self.factor
            case "s":
                for a in range(len(item.remainder)):
                    x = item.remainder[a]
                    item.remainder[a] = int(x * x)
            case _:
                raise Exception("Should not happen!")
            
        self.numberOfItemInspected += 1

        if item.number in self.seenItems:
            raise Exception("Twice same item on one Monkey")
        self.seenItems.append(item.number)

        dt = time.perf_counter() - timeBefore
        self.myGroup.inspectTime += dt

    def throw(self, item: Item):
        timeBefore = time.perf_counter()

        buff0 = item.remainder[self.number]
        buff = buff0%self.test
        item.remainder[self.number] = int(buff)


        if item.remainder[self.number] == 0:
            # self.myGroup.gr[self.trueNumber].myItems.append(item)

            if not (self.myGroup.gr[self.trueNumber].number==trueNumber or self.myGroup.gr[self.falseNumber].number==self.falseNumber):
                raise Exception("oula")
            
            if trueNumber>self.number:
                self.myGroup.gr[self.trueNumber].itemForThisTurn.append(item)
            else:
                self.myGroup.gr[self.trueNumber].itemForNextTurn.append(item)
        else:
            # self.myGroup.gr[self.falseNumber].myItems.append(item)
            if falseNumber>self.number:
                self.myGroup.gr[self.falseNumber].itemForThisTurn.append(item)
            else:
                self.myGroup.gr[self.falseNumber].itemForNextTurn.append(item)

        self.myItems.pop(0)

        dt = time.perf_counter() - timeBefore
        self.myGroup.throwTime += dt

    def playTurn(self):
        self.turnFinished = False
        itemToCheck = [item for item in self.myItems if not item.number in self.seenItems]
        for item in itemToCheck:
            self.inspect(item)
            self.throw(item)
        

    def endTurn(self):
        if self.number!=0:
            while(not self.monkeyBefore.turnFinished):
            # while(self.monkeyBefore.is_alive()):
                if self.itemForThisTurn:
                    for i in self.itemForThisTurn:
                        if not(i.number in self.seenItems):
                            self.myItems.append(i)
                    self.playTurn()
        

        for i in self.itemForThisTurn:
            if not(i.number in self.seenItems):
                self.myItems.append(i)
        self.playTurn()

        self.turnFinished = True

        self.itemForThisTurn.clear()

        if len(self.myItems)>0:
            raise Exception("Items not empty")
        
        turnEnd = False
        while(not turnEnd):
            k = 0
            for m in self.myGroup.gr:
                if not m.turnFinished:
                    k += 1
            if k==0:
                turnEnd = True

        
        self.myItems.extend(self.itemForNextTurn)
        self.itemForNextTurn.clear()
        self.seenItems.clear()
        # self.join()

    def findMonkeyBefore(self):
        if self.number == 0:
            self.monkeyBefore = None
        else:
            found = False
            for monkey in self.myGroup.gr:
                if monkey.number == (self.number-1):
                    self.monkeyBefore = monkey
                    found = True
            if not found:
                raise Exception(f"Monkey {self.number} could not find the monkey before")

    def run(self):
        self.playTurn()
        self.endTurn()

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

        self.myThreads = []

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

    def playRound(self,roundNumber):
        for monkey in self.gr:
            # monkey.playTurn()
            if roundNumber!=1:
                monkey.playTurn()
                monkey.endTurn()
            else:
                monkey.start()
        # if roundNumber==1:
        #     for monkey in self.gr:
        #         monkey.endTurn()

    def playRounds(self, numberRounds : int):
        threadLock = threading.Lock()

        for monkey in self.gr:
            monkey.findMonkeyBefore()

        for i in range(1,numberRounds+1):
            self.playRound(i)
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
        # print(f" Time to toto {round(self.toto/self.totalTime,2)*100} %")

        if final :
            res.sort()
            print(f" Monkey business is {res[-1]} x {res[-2]} = {res[-1]*res[-2]}")



monkeyGroup = MonkeyGroup()


# number : int, startingItems : list, op : str, test : int, trueNumber : int, falseNumber : int

# fileName = "test.txt"
fileName = "input.txt"

# threadLock = threading.Lock()

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
