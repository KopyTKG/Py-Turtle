import re, string
from typing import List
from copy import deepcopy as copy
from abstract import Queue, Fractal
from examples import Examples
from math import cos, sin, pi

class Turtle:
    def __init__(self, start: List,fractal: Fractal, stepLength=10):
        # default static values
        self.__validMoveCommands = ["F","A","B","C"]
        self.__validSymbols = ["+","-","[","]"]+ self.__validMoveCommands
        # user set values
        self.__stepLength = stepLength
        self.__steps = [start]
        # fractal set values
        self.__rules = fractal.rules
        self.__forwardAngle = -fractal.startAngle
        self.__loopCount = fractal.iteration
        self.__turnAngle = fractal.turnAngle
        # modified word with use of the rules
        self.__modifiedWord = self.__processRules(fractal.word)
        # parsed values
        self.__queuedWord = self.__translateMove(self.__modifiedWord)
        

    # Rule processing fuction to replace symbols with use of the rules
    def __processRules(self, word) -> str:
        translation = word.maketrans(self.__rules)
        for _ in range(self.__loopCount):
            #print(word.translate(translation))
            word = word.translate(translation)
            #for symbol in word:
            #    word = word.replace(symbol, self.__rules[symbol])
        return word

    # Takes modified word to translate it into queue of symbols
    def __translateMove(self, geneticCode) -> Queue:
        memory = Queue()
        for index, gene in enumerate(geneticCode):
            if gene in self.__validSymbols:
                memory.enqueue(gene)
        return memory

    # main function
    def run(self) -> List:
        for position in range(len(self.__queuedWord)):
            self.__doMove(self.__queuedWord.dequeue())

    # Filter function for word symbols
    def __doMove(self, symbol):
        if symbol == "+":
            self.__turnLeft()
        if symbol == "-":
            self.__turnRight()
        if symbol in self.__validMoveCommands:
            self.__move()
        
    # Move function
    def __move(self) -> None:
        oldPosition = copy(self.__steps[-1])
        newX = oldPosition[0] + (self.__stepLength * cos(self.__forwardAngle))
        newY = oldPosition[1] + (self.__stepLength * sin(self.__forwardAngle))
        newPosition = [newX, newY]
        self.__steps.append(newPosition)

    # Turn functions for turtles head
    def __turnLeft(self) -> None:
        self.__forwardAngle += self.__turnAngle

    def __turnRight(self) -> None:
        self.__forwardAngle -= self.__turnAngle

    def __iter__(self) -> List:
        for x in range(1, len(self.__steps)):
            if x <= len(self.__steps) -1:
                yield self.__steps[x-1]+ self.__steps[x]
            else:
                raise Exception("not enought steps for iteration")

def main():
    newTurtle = Turtle(
        start=[0, 0],
        stepLength=10,
        fractal=Examples.example5
    )
    newTurtle.run()

if __name__ == "__main__":
    main()