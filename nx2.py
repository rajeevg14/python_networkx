import networkx as nx
import math
g = nx.Graph()
g.add_node("spam")
g.add_edge(1,2)
g.add_node(math.cos)
print(g.nodes())
print (g.edges())
print(g.neighbors(1))
print(g.degree(1))