from manim import *

class node:
    def __init__(self, value):
        self.rn = None ##Right child node
        self.ln = None ##Left child node value
        self.val = value ##Value of this node.

class VisualGraph(Scene):
    
    def __init__(self, **kwargs):
        self.edges = []
        self.vertexes = []
        super().__init__(**kwargs)
        

    def construct(self):
        rootNode = node(1)
        self.new_node(1, rootNode)  # Populate the tree
        self.traverse(rootNode) 
        G = Graph(self.vertexes, self.edges, layout="tree", vertex_config= {"color": BLUE}, root_vertex=1,labels=True, label_fill_color=BLACK)
        self.play(Create(G))
        self.wait(2)
        
    def new_node(self, depth, Vertex):
        if depth < 4:
            Vertex.ln = node(2 * Vertex.val)
            Vertex.rn = node(2 * Vertex.val + 1)
            self.new_node(2*depth, Vertex.ln)
            self.new_node(2*depth+1, Vertex.rn)
        else:
            return
    def traverse(self, RootNode):
            Node = RootNode
            if Node.val not in self.vertexes:
                self.vertexes.append(Node.val)
            print(Node)
            if Node.ln != None:
                self.edges.append((Node.val, Node.ln.val))
                self.traverse(Node.ln)
            if Node.rn != None:
                self.edges.append((Node.val, Node.rn.val))
                self.traverse(Node.rn)
    

##Need to add the graphics now
    