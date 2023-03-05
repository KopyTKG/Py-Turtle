from typing import Any, List


class Queue:
    def __init__(self, start=[], loop=False):
        self.__loop = loop
        if not start:
            self.__memory = []
        else:
            self.__memory = start

    def isLoop(self):
        return self.__loop
    
    def enqueue(self, item) -> None:
        self.__memory.append(item)
    
    def dequeue(self) -> Any:
        return self.__memory.pop(0)

    def front(self) -> Any:
        if self.isEmpty():
            return None
        else:
            return(self.__memory[0])
    
    def rear(self) -> Any:
        if self.isEmpty():
            return None
        else:
            return(self.__memory[-1])
    
    def isEmpty(self) -> bool:
        return not self.__memory

    def size(self) -> int:
        return(len(self.__memory))

    def __len__(self) -> int:
        return self.size()

    def __repr__(self):
        reprStr = "["
        for item in self.__memory:
            if type(item) == Queue:
                reprStr += repr(item)
            else:
                reprStr += f"{item}"
        reprStr += "]"
        return reprStr

    def __str__(self) -> str:
        strRet = ""
        try:
            for item in self.__memory:
                if type(item) == Queue:
                    strRet += "(Queue)"
                else:
                    strRet += item
            return strRet
        except:
            raise Exception("Not iterable type")

    def __iter__(self):
        for item in self.__memory:
            yield item


class Fractal:
    def __init__(self, word: str, rules={"F":"F","R":"R","L":"L"}, iteration=1):
        self.__word = word
        self.__rules = rules
        self.__iteration = iteration
    
    @property
    def rules(self) -> List:
        return self.__rules
    
    @property
    def word(self) -> str:
        return self.__word
    
    @property
    def iteration(self) -> int:
        return self.__iteration

    @iteration.setter
    def iteration(self , value: int) -> None:
        self.__iteration = value
