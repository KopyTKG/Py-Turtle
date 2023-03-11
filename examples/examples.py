from core.abstract import Fractal

class Examples():
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
        iteration=5
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
    example7 = Fractal(
        word="F+F+F+F",
        rules={
            "F": "F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF",
            "-": "-",
            "+": "+",
            "f": "ffffff",
        },
        iteration=2,
        turnAngle=-90
    )

    exampleTest = Fractal(
        word="F",
        rules={
            "F": "F[+F]F[-F][F]",
            "-": "-",
            "+": "+"
        },
        iteration=5,
        turnAngle=-20
    )
    flowerTest = Fractal(
        word="X",
        rules={
            "X": "F[+X]F[-X]+X",
            "F": "FF",
            "-": "-",
            "+": "+"
        },
        iteration=7,
        turnAngle=-20
    )

    flowerTest2 = Fractal(
        word="X",
        rules={
            "X": "F[+X][-X]FX",
            "F": "FF",
            "-": "-",
            "+": "+"
        },
        iteration=7,
        turnAngle=-25.7
    )
    flowerTest3 = Fractal(
        word="F",
        rules={
            "F": "FF-[-F+F+F]+[+F-F-F]",
            "-": "-",
            "+": "+"
        },
        iteration=5,
        turnAngle=-22.5
    )