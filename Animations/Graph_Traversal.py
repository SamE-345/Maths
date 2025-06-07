import manim
from manim import *
import random as rnd

class node:
    def __init__(self, value):
        self.rn = None ##Right child node
        self.ln = None ##Left child node value
        self.val = value ##Value of this node.

##Create graph and create tree functions
class CreateGraph:
    def __init__(self, **kwargs ):
        
       
        self.vertexes = []
        self.edges = []
        self.number_Nodes = rnd.randint(4,10)
        self.Add_Edges()
        self.Add_Nodes()

    def Add_Edges(self):
        for i in range(self.number_Nodes):
            self.edges.append() = ((rnd.randint(0,self.number_Nodes-1), rnd.randint(0,self.number_Nodes-1)))

    def Add_Nodes(self):
        for i in range(self.number_Nodes):
            self.vertexes.append(i+1)

    def ReturnGraph(self):
        return manim.Graph(self.vertexes, self.edges,labels=True, label_fill_color=manim.BLACK)

class CreateWeightedGraph(CreateGraph):
    def __init__(self, **kwargs):
        self.weights = []
        super().__init__(**kwargs)
    def Add_Edges(self):
        self.edges.append() = (rnd.randint(0,self.number_Nodes-1), rnd.randint(0,self.number_Nodes-1))
        self.weights.append() = rnd.randint(0,10)

    def ReturnGraph(self):
        return manim.Graph(
            self.vertexes,
            self.edges,
            layout="circular",
            labels=True,  # Show node labels
            edge_config={e: {"label": manim.Text(str(self.weights[e]), font_size=24)} for e in self.edges}
        )


class CreateTree:
    def __init__(self, max_Depth):
        self.edges = []
        self.vertexes = []
        self.max_Depth = max_Depth

    def new_node(self, depth, Vertex):
        if depth < self.max_depth:
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

    def Return_Tree(self):
        self.traverse(self.vertexes[0])
        return manim.Graph(self.vertexes, self.edges, layout="tree", vertex_config= {"color": manim.BLUE}, root_vertex=1,labels=True, label_fill_color=manim.BLACK)
        
    

class VisualTree(manim.Scene):
    
    def __init__(self, **kwargs):
        self.edges = []
        self.vertexes = []
        super().__init__(**kwargs)
        
    def construct(self):
        G = CreateTree(5)
        self.play(manim.Create(G.Return_Tree()))
        self.wait(2)
        
    

class Dijkstra(manim.Scene): ##Should show the process of Dijkstra's shortest path.
    pass

    
    