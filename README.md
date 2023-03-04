# Py-Turtle
Turtle build in python 3.9.10

---
### File
- *abstract.py*
    - file containig custom Queue class
- *direction.py*
    - Emun needed for Turtle
- *turtle.py*
    - Turtle it self
- *master.py*
    - GUI rendering file with PyQt5
- *examples.py*
    - File with few fractal examples
---
## Use
```python
from turtle import Turtle

# init setup for turtle
turtle = Turtle(
    start=[0,0],
    word="FL",
    stepLength=10,
    iteration=1,
    rules={
        "F":"F",
        "L":"L",
        "R":"R",
    },
)

# run doest not return
turtle.run()

# to get step you need to iterate through turtle
for step in turtle:
    print(step)


# for memory hungry calculation you can use dump to file
turtle.dump()
```
### Use of examples
```python
from turtle import Turtle
from examples import Examples 

turtle = Turtle(
    start=[0,0],
    # here you can choose between example words
    word=Examples.word["example1"],
    stepLength=10,
    iteration=1,
    # same with rules
    rules=Examples.rules["example1"],
)

turtle.run()

for step in turtle:
    print(step)

```
for more info look into **Example.py**
### Rule symbols
- **F** - forward move by step lenght
- **R** - turn to right side
- **L** - turn to left side
- **[** - begin loop
- **]** - end loop
---
