# Py-Turtle
Turtle build in python 3.9.10

---
### File
- [*abstract.py*](./core/abstract.py)
    - file containig custom Queue class and Fractal class
- [*turtle.py*](./core/turtle.py)
    - Turtle it self
- [*master.py*](./master.py)
    - GUI rendering file with PyQt5
- [*examples.py*](./exmaples/examples.py)
    - File with few fractal examples
- [*DOLsystem.py*](./exmaples/DOLsystem.py)
    - File with few fractal DOL-systems examples (**The iteration needs to be edited by user**)
---
## Use
```python
from core.turtle import Turtle
from core.abstract import Fractal

#define fractal
newFractal = Fractal(
    #starting word
    word="+F",
    #rewriting rules
    rules={
        "F": "F-F+F+F-F",
        "-": "-",
        "+": "+" 
    },
    #turn angle
    turnAngle=90,
    #iterations (choose wisly)
    iteration=6,
    #if needed you can change starting angle
    startAngle=90 #default 90
)

# init setup for turtle
turtle = Turtle(
    start=[0,0],
    stepLength=10,
    fractal=newFractal
)
# run doest not return
turtle.run()

# to get step you need to iterate through turtle
for step in turtle:
    print(step)

```
#### for use of examples follow this
### Use of examples
```python
from core.turtle import Turtle
from examples.examples import Examples, DOLsystem

turtle = Turtle(
    start=[0,0],
    stepLength=10,
    # for use of examples or DOLsystem
    fractal=Examples.example1
)

turtle.run()

for step in turtle:
    print(step)

```
---
### Rule symbols
- **F** \ **A** \ **B** \ **C** \ **X**
     - all symbols used for movement by step lenght and Draw line
- **f** \ **a** \ **b** \ **c** \ **x**
    - all symbols used to just move forward
- **-** \ **R** - turn to right side
- **+** \ **L** - turn to left side
- **[** - turtle save symbol
- **]** - turtle load symbol
for more info about commands look into [**config.yaml**](./config/config.yaml)

---
