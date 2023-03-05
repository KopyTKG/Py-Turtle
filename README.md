# Py-Turtle
Turtle build in python 3.9.10

---
### File
- [*abstract.py*](./abstract.py)
    - file containig custom Queue class and Fractal class
- [*turtle.py*](./turtle.py)
    - Turtle it self
- [*master.py*](./master.py)
    - GUI rendering file with PyQt5
- [*examples.py*](./examples.py)
    - File with few fractal examples
---
## Use
```python
from turtle import Turtle
from fractal import Fractal

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


# for memory hungry calculation you can use dump to file
turtle.dump()
```
#### for use of examples follow this
### Use of examples
```python
from turtle import Turtle
from examples import Examples 

turtle = Turtle(
    start=[0,0],
    stepLength=10,
    # for use of examples
    fractal=Examples.example1
)

turtle.run()

for step in turtle:
    print(step)

```
for more info look into [**examples.py**](./examples.py)
### Rule symbols
- **F** \ **A** \ **B** \ **C**
     - all symbols used for movement by step lenght
- **-** - turn to right side
- **+** - turn to left side
---
