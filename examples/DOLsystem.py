from core.abstract import Fractal

# Simplest class of L-system 
# Deterministic and context-free
class DOLsystem():
    KochIsland = Fractal(
        word="F-F-F-F",
        rules={
            "F":"F-F+F+FF-F-F+F",
            "-":"-",
            "+":"+"
        },
        turnAngle=-90,
        iteration=1
        )
    
    QuadraticKochIsland = Fractal(
        word="F-F-F-F", 
        rules={
            "F":"F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F",        
            "+":"+",    
            "-":"-"    
        },
        turnAngle=-90,
        iteration=1
        )

    QuadraticSnowFlakeCurve = Fractal(
        word="-F",
        rules={
            "F": "F+F-F-F+F",
            "-": "-",
            "+": "+" 
        },
        turnAngle=-90,
        iteration=1
        )