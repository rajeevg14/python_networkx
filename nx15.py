import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph() #or G = nx.MultiDiGraph()
G.add_node('A')
G.add_node('B')
G.add_edge('A', 'B', length = 2)
G.add_edge('B', 'A', length = 3)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
edge_labels=dict([((u,v,),d['length'])
             for u,v,d in G.edges(data=True)])

plt.show()
