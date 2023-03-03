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
---
## Use
```python
from turtle import Turtle

# init setup for turtle
turtle = Turtle(
    start=[0,0],
    geneticCode="[FL]",
    stepLength=10,
    loopCount=4
)

# run doest not return
turtle.run()

# to get step you need to iterate through turtle
for step in turtle:
    print(step)

```
### Genetic Code
- **F** - forward move by step lenght
- **R** - turn to right side
- **L** - turn to left side
- **[** - begin loop
- **]** - end loop
---
