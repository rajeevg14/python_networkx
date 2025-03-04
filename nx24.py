import matplotlib.pyplot as plt
import networkx as nx

G = nx.cycle_graph(10)
A = nx.adjacency_matrix(G)

print(A.todense())
G.add_edge(1,5)
nx.draw_networkx(G)
plt.show()

