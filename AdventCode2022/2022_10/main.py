
# fileName = "test.txt"
fileName = "input.txt"

data = []
with open(fileName) as file:
    line = file.readline().strip("\n")
    while line:
        data.append(line)
        line = file.readline().strip("\n")

class Device:
        def __init__(self) -> None:
            self.numberCycle = 0
            self.X = 1
            # self.cyleToStop = [-20+i*40 for i in range(1,7)]
            self.cyleToStop = [i*40 for i in range(1,7)]
            self.signalStrength = []
            self.wholeSignal = []
            self.signalCurrentLine = ""

        def addCycle(self):
            self.numberCycle += 1
            self.draw()
            self.checkSignal()

        def draw(self):
            pixelPosition = len(self.signalCurrentLine)
            if pixelPosition in [self.X-1,self.X,self.X+1]:
                newChar = "#"
            else:
                newChar = "."
            self.signalCurrentLine += newChar

        def checkSignal(self):
            if self.numberCycle in self.cyleToStop:
                self.wholeSignal.append(self.signalCurrentLine)
                self.signalCurrentLine = ""
                # self.signalStrength.append(self.numberCycle*self.X)

myDevice = Device()

for line in data:    
    instruction = line.split(" ")[0]

    match instruction:
        case "addx":
            myDevice.addCycle()
            myDevice.addCycle()
            value = line.split(" ")[1]
            myDevice.X += int(value)
        case "noop":
            myDevice.addCycle()

# print(myDevice.signalStrength)
# print(sum(myDevice.signalStrength))
space = 5
for i in range(space):
    print("\n")

for line in myDevice.wholeSignal:
    print(line)

for i in range(space):
    print("\n")