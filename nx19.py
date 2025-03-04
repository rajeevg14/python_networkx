import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["E","F"],
    "D":["B","G"],
    "E":["B","C"],
    "F":["C","G"],
    "G":["D","F"]
}
x=10
for vertex, edges in graph.items():
    G.add_node("%s" % vertex)
    x+=2
    for edge in edges:
        G.add_node("%s" % edge)
        G.add_edge("%s" % vertex, "%s" % edge, weight = x)
        print("'%s' it connects with '%s'" % (vertex,edge))
# ---- END OF UNCHANGED CODE ----

# Create positions of all nodes and save them
pos = nx.spring_layout(G)

# Draw the graph according to node positions
nx.draw(G, pos, with_labels=True)

# Create edge labels
labels = {e: str(e) for e in G.edges}

# Draw edge labels according to node positions
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()