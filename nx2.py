import networkx as nx
g = nx.Graph()
g.add_node("spam")
g.add_edge(1,2)
print(g.nodes())
print (g.edges())