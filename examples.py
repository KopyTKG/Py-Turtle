from abstract import Fractal

class Examples():
    example1 = Fractal(
        word="+F",
        rules={
            "F": "F-F+F+F-F",
            "-": "-",
            "+": "+" 
        },
        turnAngle=90,
        iteration=6
    )
    example2 = Fractal(
        word="F+F+F+F",
        rules={
            "F": "FF+F++F+F",
            "-": "-",
            "+": "+" 
        },
        turnAngle=90,
        iteration=5
    )
    example3 = Fractal(
        word="F+F+F+F",
        rules={
            "F": "F-FF--F-F",
            "-": "-",
            "+": "+" 
        },
        turnAngle=90,
        iteration=8
    )
    example4 = Fractal(
        word="B",
        rules={
            "A": "B-A-B",
            "B": "A+B+A",
            "-": "-",
            "+": "+",
        },
        iteration=10,
        startAngle=60,
        turnAngle=60
    )
    example5 = Fractal(
        word="F+F+F+F",
        rules={
            "F": "FF+F+F+F+FF",
            "-": "-",
            "+": "+",
        },
        iteration=5,
        turnAngle=90
    )
    example6 = Fractal(
        word="F-F-F-F",
        rules={
            "F": "FF-F+F-F-FF",
            "-": "-",
            "+": "+",
        },
        iteration=5,
        turnAngle=90
    )
    exampleList = [example1,example2,example3,example4,example5,example6]