from manim import *

class node:
    def __init__(self, value):
        self.rn = -1 ##Right child node
        self.ln = -1 ##Left child node value
        self.val = value ##Value of this node.

class VisualGraph:
    
    def __init__(self):
        pass
    def construct(self):
        i = 0
        RootNode = node(0)
        self.new_node(RootNode, 0)
        
    def new_node(self, val, Vertex):
        if val<8:
            Vertex.ln = self.new_node(2**(val+1))
            Vertex.rn = self.new_node(2**(val+2))
        else:
            return
    def traverse(self, RootNode):
            Node = RootNode
            print(Node)
            if Node.ln != -1:
                self.traverse(Node.ln)
            if Node.rn != -1:
                self.traverse(Node.rn)
        
##Need to add the graphics now
    