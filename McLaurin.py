import manim
import math
from manim import *

class SinWave(Scene):
    def construct(self):
        ax = Axes(x_range=[-4*3.14, 4*3.14],
                  y_range=[-1,1],  tips=False,
            axis_config={"include_numbers": True})
        
        self.play(FadeIn(ax))
        
        self.Create_function(3,7, lambda x: x, False)
        Curve = ax.plot(self.Function)
        Curve.color = random_bright_color()
        self.play(Create(Curve))
        self.wait(2)
       

    def Create_function(self, n, max_val, Funct, sign):
        if(n>max_val):
            self.Function =Funct
        else:
            num = 2*n+1
            sin = lambda x: ((x**num)/(math.factorial(num)))
            if(sign == True):
                Function =lambda x: (Funct(x) + sin(x))
                sign = False
            else:
                Function =lambda x: (Funct(x) - sin(x))
                sign = True
            self.Create_function(n+1, max_val, Function, sign)
        
class CosWave(Scene):
    def construct(self):
        ax = Axes(x_range=[-4*3.14, 4*3.14],
                  y_range=[-1,1],  tips=False,
            axis_config={"include_numbers": True})
        
        self.play(FadeIn(ax))
        for i in range(4):
            self.Create_function(3,i*4, lambda x: 1, False)
            Curve = ax.plot(self.Function)
            Curve.color = random_bright_color()
            self.play(Create(Curve))
            self.wait(2)
        self.wait(4)

    def Create_function(self, n, max_val, Funct, sign):
        if(n>max_val):
            self.Function =Funct
        else:
            num = 2*n+1
            cos = lambda x: (x**num)/(math.factorial(num))
            if(sign == True):
                Function =lambda x: Funct(x) + cos(x)
                sign = False
            else:
                Function =lambda x: Funct(x) - cos(x)
                sign = True
            self.Create_function(n+1, max_val, Function, sign)
        
                