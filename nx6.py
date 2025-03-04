import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edges_from([(1 ,2) , (2 ,3) , (1 ,3) , (1 ,4) ])
pos = { 1: (20, 30), 2: (40, 30), 3: (30, 10),4: (0, 40)} 

nx.draw_networkx(G, pos=pos)

plt.show()