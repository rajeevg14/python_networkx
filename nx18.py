import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from netgraph import Graph # pip install netgraph

triangle = nx.DiGraph([('a', 'b'), ('a', 'c'), ('b', 'a'), ('c', 'b'), ('c', 'c')])

node_positions = {
    'a' : np.array([0.2, 0.2]),
    'b' : np.array([0.8, 0.2]),
    'c' : np.array([0.5, 0.8]),
}

edge_labels = {
    ('a', 'b') : 3,
    ('a', 'c') : 'Lorem ipsum',
    ('b', 'a') : 4,
    ('c', 'b') : 'dolor sit',
    ('c', 'c') : r'$\pi$'
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,14))

Graph(triangle, node_labels=True, edge_labels=edge_labels,
      edge_label_fontdict=dict(size=12, fontweight='bold'),
      node_layout=node_positions, edge_layout='straight',
      node_size=6, edge_width=4, arrows=True, ax=ax1)

Graph(triangle, node_labels=True, edge_labels=edge_labels,
      edge_label_fontdict=dict(size=12, fontweight='bold'),
      node_layout=node_positions, edge_layout='curved',
      node_size=6, edge_width=4, arrows=True, ax=ax2)

plt.show()