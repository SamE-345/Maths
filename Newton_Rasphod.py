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
        self.add(ax)
        graph = ax.plot(lambda x: x ** 2, x_range=[-10, 10], use_smoothing=False)
        graph.stroke_color = GREEN
        self.add(ax, graph)
        startpoint = 9
        for i in range(5):
            gradient = lambda a: 2*a 
            plot = lambda b: b**2
            tangent = ax.plot(lambda x: ((startpoint*x*2)- startpoint**2))
            
            self.add(tangent)
            startpoint = (startpoint - (plot(startpoint)/gradient(startpoint)))

    




