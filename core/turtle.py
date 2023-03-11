import re, string
from typing import List
from copy import deepcopy as copy
from core.abstract import Queue, Fractal, Stack, Status
from math import cos, sin, pi

class Turtle:
    def __init__(self, start: List,fractal: Fractal, stepLength=10,):
        # default static values
        self.__validMoveCommands = ["F","A","B","C","X"]
        self.__validSkipCommands = ["f"]
        self.__validSymbols = ["+","-","[","]",]+ self.__validMoveCommands+ self.__validSkipCommands
        # user set values
        self.__stepLength = stepLength
        self.__steps = []
        # fractal set values
        self.__rules = fractal.rules
        self.__forwardAngle = -fractal.startAngle
        self.__loopCount = fractal.iteration
        self.__turnAngle = fractal.turnAngle
        # modified word with use of the rules
        self.__modifiedWord = self.__processRules(fractal.word)
        self.__savedStatus = Stack()
        # parsed values
        self.__queuedWord = self.__translateMove(self.__modifiedWord)
        self.__lastPosition = start
        self.__lastPoint = []

    # Rule processing fuction to replace symbols with use of the rules
    def __processRules(self, word) -> str:
        translation = word.maketrans(self.__rules)
        for _ in range(self.__loopCount):
            #print(word.translate(translation))
            word = word.translate(translation)
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
        if symbol in self.__validMoveCommands or symbol in self.__validSkipCommands:
            self.__move(symbol)
        if symbol == "[":
            self.__saveTurtleStep()
        if symbol == "]":
            self.__loadTurtleStep()
        
    # Move function
    def __move(self, symbol) -> None:
        print(self.__lastPoint)
        # Get current position
        self.__lastPoint.append(self.__lastPosition)

        # Calculate new position
        newX =  self.__lastPosition[0] + (self.__stepLength * cos(self.__forwardAngle))
        newY =  self.__lastPosition[1] + (self.__stepLength * sin(self.__forwardAngle))
        newPosition = [newX, newY]

        # Check if the pen is down
        if symbol in self.__validMoveCommands:
            self.__lastPoint.append(newPosition)
            self.__steps.append(self.__lastPoint)
        # reset lastPoint and last position
        self.__lastPosition = newPosition
        self.__lastPoint = []


    # Turn functions for turtles head
    def __turnLeft(self) -> None:
        self.__forwardAngle += self.__turnAngle

    def __turnRight(self) -> None:
        self.__forwardAngle -= self.__turnAngle

    def __saveTurtleStep(self) -> None:
        position = self.__lastPosition
        angle = self.__forwardAngle
        newStatus = Status(position=position, angle=angle)
        self.__savedStatus.push(newStatus)

    def __loadTurtleStep(self) -> None:
        lastStatus = self.__savedStatus.pop()
        self.__forwardAngle = lastStatus.angle
        self.__lastPosition = lastStatus.position

    def __iter__(self) -> List:
        for step in self.__steps:         
            yield step[0]+step[1]