from abstract import Fractal

class Examples():
    example1 = Fractal(
        word="LF",
        rules={
            "F": "FRFLFLFRF",
            "R": "R",
            "L": "L" 
        },
        iteration=2
    )
    example2 = Fractal(
        word="FLFLFLF",
        rules={
            "F": "FFLFLLFLF",
            "R": "R",
            "L": "L" 
        },
        iteration=1
    )
    example3 = Fractal(
        word="FLFLFLF",
        rules={
            "F": "FRFFRRFRF",
            "R": "R",
            "L": "L" 
        },
        iteration=1
    )