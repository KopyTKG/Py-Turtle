import re
from typing import List
from copy import deepcopy as copy
from abstract import Queue, Fractal
from direction import Direction
import uuid

class Turtle:
    def __init__(self, start: List,fractal: Fractal, stepLength=10):
        self.__stepLength = stepLength
        self.__steps = [start]
        self.__direction = Direction.UP
        self.__rules = fractal.rules
        self.__loopCount = fractal.iteration
        self.__parsedWord = self.__processRules(fractal.word)
        self.__geneticCode = self.__translateMove(self.__parsedWord)
        self.__degreeStr = ""

        self.__directionMapLeft = {
                Direction.UP: Direction.LEFT,
                Direction.LEFT: Direction.DOWN,
                Direction.DOWN: Direction.RIGHT,
                Direction.RIGHT: Direction.UP
               }

        self.__directionMapRight = {
                Direction.UP: Direction.RIGHT,
                Direction.RIGHT: Direction.DOWN,
                Direction.DOWN: Direction.LEFT,
                Direction.LEFT: Direction.UP
               }

    def __processRules(self, word) -> str:
        for _ in range(self.__loopCount):
            for symbol in word:
                word = word.replace(symbol, self.__rules[symbol])
        return word

    def __translateMove(self, geneticCode) -> Queue:
        valid = ["F","L","R"]
        memory = Queue(loop=(geneticCode[0] == "["))
        if memory.isLoop():
            geneticCode = geneticCode[1:-1]

        skipTo = -1
        for index, gene in enumerate(geneticCode):
            if gene == "[":
                loop = Queue(loop=True)
                for loopIndex in range(index, len(geneticCode)):
                    if geneticCode[loopIndex] == "]":
                        skipTo = loopIndex
                        break
                    elif geneticCode[loopIndex] in valid:
                        loop.enqueue(geneticCode[loopIndex])
                memory.enqueue(loop)
            elif gene in valid and skipTo < index:
                memory.enqueue(gene)

        return memory

    def __mainLoop(self, code):
        for position in range(len(code)):
            if type(code.front()) == Queue:
                if code.front().isLoop():
                    front = code.dequeue()
                    for _ in range(self.__loopCount):
                        for innerPosition in range(len(front)):
                            memory = copy(front)
                            while not memory.isEmpty():
                                self.__doMove(memory.dequeue())
                else:
                    front = code.dequeue()
                    for innerPosition in range(len(front)):
                        memory = copy(front)
                        while not memory.isEmpty():
                                self.__doMove(memory.dequeue())
            else:
                self.__doMove(code.dequeue())

    def run(self) -> List:
        activeLoop = False
        if not self.__geneticCode.isLoop():
            self.__mainLoop(self.__geneticCode)
        else:
            for _ in range(self.__loopCount):
                self.__mainLoop(copy(self.__geneticCode))
        return self.__steps

    def __doMove(self, symbol):
        if symbol == "L":
            self.__turnLeft()
        if symbol == "R":
            self.__turnRight()
        if symbol == "F":
            self.__move()
        
    def __move(self) -> None:
        oldPosition = copy(self.__steps[-1])
        if self.__direction == Direction.UP:
            newPosition = [oldPosition[0], oldPosition[1]-self.__stepLength]
            self.__steps.append(newPosition)

        if self.__direction == Direction.DOWN:
            newPosition = [oldPosition[0], oldPosition[1]+self.__stepLength]
            self.__steps.append(newPosition)

        if self.__direction == Direction.LEFT:
            newPosition = [oldPosition[0]-self.__stepLength, oldPosition[1]]
            self.__steps.append(newPosition)

        if self.__direction == Direction.RIGHT:
            newPosition = [oldPosition[0]+self.__stepLength, oldPosition[1]]
            self.__steps.append(newPosition)

    def __turnLeft(self) -> None:
        self.__direction = self.__directionMapLeft[self.__direction]

    def __turnRight(self) -> None:
        self.__direction = self.__directionMapRight[self.__direction]

    def __iter__(self) -> List:
        for x in range(1, len(self.__steps)):
            if x <= len(self.__steps) -1:
                yield self.__steps[x-1]+ self.__steps[x]
            else:
                raise Exception("not enought steps for iteration")

def main():
    newTurtle = Turtle(
        start=[1920, 1080],
        word="LF",
        stepLength=1,
        iteration=2,
        rules={
            "F": "FRFLFLFRF",
            "R": "R",
            "L": "L" 
        }
    )
    newTurtle.run()
    print(newTurtle.dump())
    
if __name__ == "__main__":
    main()