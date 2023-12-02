# --- Day 9: Rope Bridge ---
# This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

# It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.

# You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where not to step.

# Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.

# Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move.

# Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):

# ....
# .TH.
# ....

# ....
# .H..
# ..T.
# ....

# ...
# .H. (H covers T)
# ...
# If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:

# .....    .....    .....
# .TH.. -> .T.H. -> ..TH.
# .....    .....    .....

# ...    ...    ...
# .T.    .T.    ...
# .H. -> ... -> .T.
# ...    .H.    .H.
# ...    ...    ...
# Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:

# .....    .....    .....
# .....    ..H..    ..H..
# ..H.. -> ..... -> ..T..
# .T...    .T...    .....
# .....    .....    .....

# .....    .....    .....
# .....    .....    .....
# ..H.. -> ...H. -> ..TH.
# .T...    .T...    .....
# .....    .....    .....
# You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.

# For example:

# R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference point):

# == Initial State ==

# ......
# ......
# ......
# ......
# H.....  (H covers T, s)

# == R 4 ==

# ......
# ......
# ......
# ......
# TH....  (T covers s)

# ......
# ......
# ......
# ......
# sTH...

# ......
# ......
# ......
# ......
# s.TH..

# ......
# ......
# ......
# ......
# s..TH.

# == U 4 ==

# ......
# ......
# ......
# ....H.
# s..T..

# ......
# ......
# ....H.
# ....T.
# s.....

# ......
# ....H.
# ....T.
# ......
# s.....

# ....H.
# ....T.
# ......
# ......
# s.....

# == L 3 ==

# ...H..
# ....T.
# ......
# ......
# s.....

# ..HT..
# ......
# ......
# ......
# s.....

# .HT...
# ......
# ......
# ......
# s.....

# == D 1 ==

# ..T...
# .H....
# ......
# ......
# s.....

# == R 4 ==

# ..T...
# ..H...
# ......
# ......
# s.....

# ..T...
# ...H..
# ......
# ......
# s.....

# ......
# ...TH.
# ......
# ......
# s.....

# ......
# ....TH
# ......
# ......
# s.....

# == D 1 ==

# ......
# ....T.
# .....H
# ......
# s.....

# == L 5 ==

# ......
# ....T.
# ....H.
# ......
# s.....

# ......
# ....T.
# ...H..
# ......
# s.....

# ......
# ......
# ..HT..
# ......
# s.....

# ......
# ......
# .HT...
# ......
# s.....

# ......
# ......
# HT....
# ......
# s.....

# == R 2 ==

# ......
# ......
# .H....  (H covers T)
# ......
# s.....

# ......
# ......
# .TH...
# ......
# s.....
# After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram, s again marks the starting position (which the tail also visited) and # marks other positions the tail visited:

# ..##..
# ...##.
# .####.
# ....#.
# s###..
# So, there are 13 positions the tail visited at least once.

# Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?


# --- Part Two ---
# A rope snaps! Suddenly, the river is getting a lot closer than you remember. The bridge is still there, but some of the ropes that broke are now whipping toward you as you fall through the air!

# The ropes are moving too quickly to grab; you only have a few seconds to choose how to arch your body to avoid being hit. Fortunately, your simulation can be extended to support longer ropes.

# Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head of the rope and moves according to the series of motions. Each knot further down the rope follows the knot in front of it using the same rules as before.

# Using the same series of motions as the above example, but with the knots marked H, 1, 2, ..., 9, the motions now occur as follows:

# == Initial State ==

# ......
# ......
# ......
# ......
# H.....  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)

# == R 4 ==

# ......
# ......
# ......
# ......
# 1H....  (1 covers 2, 3, 4, 5, 6, 7, 8, 9, s)

# ......
# ......
# ......
# ......
# 21H...  (2 covers 3, 4, 5, 6, 7, 8, 9, s)

# ......
# ......
# ......
# ......
# 321H..  (3 covers 4, 5, 6, 7, 8, 9, s)

# ......
# ......
# ......
# ......
# 4321H.  (4 covers 5, 6, 7, 8, 9, s)

# == U 4 ==

# ......
# ......
# ......
# ....H.
# 4321..  (4 covers 5, 6, 7, 8, 9, s)

# ......
# ......
# ....H.
# .4321.
# 5.....  (5 covers 6, 7, 8, 9, s)

# ......
# ....H.
# ....1.
# .432..
# 5.....  (5 covers 6, 7, 8, 9, s)

# ....H.
# ....1.
# ..432.
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# == L 3 ==

# ...H..
# ....1.
# ..432.
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# ..H1..
# ...2..
# ..43..
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# .H1...
# ...2..
# ..43..
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# == D 1 ==

# ..1...
# .H.2..
# ..43..
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# == R 4 ==

# ..1...
# ..H2..
# ..43..
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# ..1...
# ...H..  (H covers 2)
# ..43..
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# ......
# ...1H.  (1 covers 2)
# ..43..
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# ......
# ...21H
# ..43..
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# == D 1 ==

# ......
# ...21.
# ..43.H
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# == L 5 ==

# ......
# ...21.
# ..43H.
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# ......
# ...21.
# ..4H..  (H covers 3)
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# ......
# ...2..
# ..H1..  (H covers 4; 1 covers 3)
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# ......
# ...2..
# .H13..  (1 covers 4)
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# ......
# ......
# H123..  (2 covers 4)
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# == R 2 ==

# ......
# ......
# .H23..  (H covers 1; 2 covers 4)
# .5....
# 6.....  (6 covers 7, 8, 9, s)

# ......
# ......
# .1H3..  (H covers 2, 4)
# .5....
# 6.....  (6 covers 7, 8, 9, s)
# Now, you need to keep track of the positions the new tail, 9, visits. In this example, the tail never moves, and so it only visits 1 position. However, be careful: more types of motion are possible than before, so you might want to visually compare your simulated rope to the one above.

# Here's a larger example:

# R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20
# These motions occur as follows (individual steps are not shown):

# == Initial State ==

# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ...........H..............  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................

# == R 5 ==

# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ...........54321H.........  (5 covers 6, 7, 8, 9, s)
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................

# == U 8 ==

# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ................H.........
# ................1.........
# ................2.........
# ................3.........
# ...............54.........
# ..............6...........
# .............7............
# ............8.............
# ...........9..............  (9 covers s)
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................

# == L 8 ==

# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ........H1234.............
# ............5.............
# ............6.............
# ............7.............
# ............8.............
# ............9.............
# ..........................
# ..........................
# ...........s..............
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................

# == D 3 ==

# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# .........2345.............
# ........1...6.............
# ........H...7.............
# ............8.............
# ............9.............
# ..........................
# ..........................
# ...........s..............
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................

# == R 17 ==

# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ................987654321H
# ..........................
# ..........................
# ..........................
# ..........................
# ...........s..............
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................

# == D 10 ==

# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ...........s.........98765
# .........................4
# .........................3
# .........................2
# .........................1
# .........................H

# == L 25 ==

# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ...........s..............
# ..........................
# ..........................
# ..........................
# ..........................
# H123456789................

# == U 20 ==

# H.........................
# 1.........................
# 2.........................
# 3.........................
# 4.........................
# 5.........................
# 6.........................
# 7.........................
# 8.........................
# 9.........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ...........s..............
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................

# Now, the tail (9) visits 36 positions (including s) at least once:

# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................
# #.........................
# #.............###.........
# #............#...#........
# .#..........#.....#.......
# ..#..........#.....#......
# ...#........#.......#.....
# ....#......s.........#....
# .....#..............#.....
# ......#............#......
# .......#..........#.......
# ........#........#........
# .........########.........
# Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?

import matplotlib.pyplot as plt

# fileName = "test.txt"
fileName = "input.txt"

with open(fileName) as file:
    data = file.readlines()

# visitedPositions = {"0_0"}

class Tail:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

class Head:
    def __init__(self,tail : Tail) -> None:
        self.x=0
        self.y=0
        self.myTail = tail

    def move(self,line):
        direction = line.split(" ")[0]
        distance = int(line.split(" ")[1])
        match direction:
            case "R":
                for i in range(distance):
                    self.moveRight()
            case "L":
                for i in range(distance):
                    self.moveLeft()
            case "D":
                for i in range(distance):
                    self.moveDown()
            case "U":
                for i in range(distance):
                    self.moveUp()
    
    def moveRight(self):
        self.x += 1
        if not(abs(self.x-self.myTail.x)<=1):
            self.myTail.x += 1
            if self.y!=self.myTail.y:
                self.myTail.y = self.y

        visitedPositions.add(str(self.myTail.x)+"_"+str(self.myTail.y))

    def moveLeft(self):
        self.x -= 1
        if not(abs(self.x-self.myTail.x)<=1):
            self.myTail.x -= 1
            if self.y!=self.myTail.y:
                self.myTail.y = self.y

        visitedPositions.add(str(self.myTail.x)+"_"+str(self.myTail.y))

    def moveDown(self):
        self.y -= 1
        if not(abs(self.y-self.myTail.y)<=1):
            self.myTail.y -= 1
            if self.x!=self.myTail.x:
                self.myTail.x = self.x

        visitedPositions.add(str(self.myTail.x)+"_"+str(self.myTail.y))

    def moveUp(self):
        self.y += 1
        if not(abs(self.y-self.myTail.y)<=1):
            self.myTail.y += 1
            if self.x!=self.myTail.x:
                self.myTail.x = self.x

        visitedPositions.add(str(self.myTail.x)+"_"+str(self.myTail.y))

# QUESTION 1

# myTail = Tail()
# myHead = Head(myTail)

# for line in data:
#     line = line.strip("\n")
#     myHead.move(line)

# print(f"Number of visited positions : {len(visitedPositions)}")


## QUESTION 2

visitedPositions = {"0_0"}
visitedPosListX = [0]
visitedPosListY = [0]

PlotCurves = False

class Head2:
    def __init__(self) -> None:
        self.x=0
        self.y=0
        self.knotAfter = None
        self.number = "H"

        self.displacement = [0,0]

    def move(self,line):
        direction = line.split(" ")[0]
        distance = int(line.split(" ")[1])
        match direction:
            case "R":
                for i in range(distance):
                    self.moveRight()
                    if (PlotCurves):
                        plotRope()
            case "L":
                for i in range(distance):
                    self.moveLeft()
                    if (PlotCurves):
                        plotRope()
            case "D":
                for i in range(distance):
                    self.moveDown()
                    if (PlotCurves):
                        plotRope()
            case "U":
                for i in range(distance):
                    self.moveUp()
                    if (PlotCurves):
                        plotRope()    
    def moveRight(self):
        self.x += 1
        self.displacement = [1,0]
        self.knotAfter.follow()

    def moveLeft(self):
        self.x -= 1
        self.displacement = [-1,0]
        self.knotAfter.follow()

    def moveDown(self):
        self.y -= 1
        self.displacement = [0,-1]
        self.knotAfter.follow()

    def moveUp(self):
        self.y += 1
        self.displacement = [0,1]
        self.knotAfter.follow()

class Knot:
    def __init__(self,knotBefore, number : str, tail : bool = False) -> None:
        self.x=0
        self.y=0

        self.displacement = [0,0]

        self.knotBefore = knotBefore
        knotBefore.knotAfter = self
        self.knotAfter = None

        self.number = number

        self.tail = tail

    def follow(self):
        self.displacement = [0,0]
        if (abs(self.knotBefore.x-self.x)>1) or (abs(self.knotBefore.y-self.y)>1):
            if (self.knotBefore.displacement[0]!= 0) and (self.knotBefore.displacement[1]!= 0):
                if self.x != self.knotBefore.x and self.y != self.knotBefore.y:
                    self.displacement[:] = self.knotBefore.displacement[:]
                    self.x += self.displacement[0]
                    self.y += self.displacement[1]
                elif self.x == self.knotBefore.x:
                    self.displacement[0] = 0
                    self.displacement[1] = self.knotBefore.displacement[1]
                    self.y += self.displacement[1]
                elif self.y == self.knotBefore.y:
                    self.displacement[1] = 0
                    self.displacement[0] = self.knotBefore.displacement[0]
                    self.x += self.displacement[0]

            elif(self.knotBefore.displacement[0]!= 0):
                self.displacement[0] = self.knotBefore.displacement[0]
                self.x += self.displacement[0]
                oldY = self.y
                self.y = self.knotBefore.y
                self.displacement[1] = self.y - oldY
            elif(self.knotBefore.displacement[1]!= 0):
                self.displacement[1] = self.knotBefore.displacement[1]
                self.y += self.displacement[1]
                oldX = self.x
                self.x = self.knotBefore.x
                self.displacement[0] = self.x - oldX
            else:
                raise Exception(f"Should not happen, disp : {self.knotBefore.displacement}")

        if not self.tail:
            self.knotAfter.follow()
        else:
            visitedPositions.add(str(self.x)+"_"+str(self.y))
            visitedPosListX.append(self.x)
            visitedPosListY.append(self.y)

length = 9
rope = []
myHead = Head2()
rope.append(myHead)
knot = Knot(knotBefore=myHead, number="1")
rope.append(knot)
for i in range(2,length):
    newKnot = Knot(knotBefore=knot, number=str(i))
    rope.append(newKnot)
    knot = newKnot
tail = Knot(knotBefore=knot,number=str(9),tail=True)
rope.append(tail)

print(f"Legth of rope : {len(rope)}")


def plotRope():
    listPosX = [knot.x for knot in rope]
    listPosY = [knot.y for knot in rope]
    fig ,ax = plt.subplots()
    ax.scatter(listPosX,listPosY)

    for i in range(length+1):
        ax.annotate(str(i if i else "H"),(listPosX[i],listPosY[i]))
    ax.grid()
    plt.show()

# fileName = "test2.txt"
fileName = "input.txt"

with open(fileName) as file:
    data = file.readlines()

for line in data:
    line = line.strip("\n")
    # print(line)
    myHead.move(line)

    # plotRope()




print(f"Number of visited positions : {len(visitedPositions)}")


plt.plot(visitedPosListX,visitedPosListY)
plt.show()