import matplotlib.pyplot as plt
import networkx as nx

from netgraph import Graph # pip install netgraph

g = nx.florentine_families_graph()
Graph(g, edge_layout='curved')
plt.show()