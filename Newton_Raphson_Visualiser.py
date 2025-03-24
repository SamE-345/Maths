import manim as manim
print(manim.__Version__)
from manim import *
import math

from manim import Scene, Axes, WHITE, GREEN

class NRMethod(Scene):
    
    def construct(self):
        ax = Axes(  
        axis_config={ "include_numbers": True},
        x_range=[-10, 10, 1],
        y_range=[0, 100, 10],
        )
        ax.stroke_color = WHITE
        function = lambda x: x ** 2
        graph = ax.plot(function, x_range=[-10, 10], use_smoothing=False)
        graph.stroke_color = GREEN
        self.play(Create(ax))
        self.play(Create(graph))
        x0 = 9
        points=[]
        for i in range(5):
          
            y0 = function(x0)
            gradient = 2*x0 # Change gradient to fit the function
            tangent = ax.plot(lambda x: gradient*(x-x0)+y0, x_range=[-10, 10], color=random_bright_color())
            
            point = Dot(ax.c2p(x0, y0), color=YELLOW)
            x0 = x0 - (function(x0))/gradient
            points.append(point)
            self.play(FadeIn(point))
            self.play(Create(tangent), run_time=1)
            self.wait(1)
            
    




