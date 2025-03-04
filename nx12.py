import networkx as nx
import gravis as gv

edges = [
    ('A', 'B', 1, 'black'),
    ('B', 'C', 3, 'black'),
    ('B', 'D', 2, 'black'),
    ('B', 'E', 1, 'black'),
    ('C', 'D', 1, 'red'),
    ('C', 'E', 4, 'black'),
    ('D', 'A', 2, 'red'),
    ('D', 'E', 2, 'black'),
    ('E', 'F', 3, 'black'),
    ('G', 'D', 1, 'black'),
]
g = nx.DiGraph()
for source, target, strength, color in edges:
    g.add_edge(source, target, strength=strength, color=color)

fig = gv.d3(g, show_edge_label=True, edge_label_data_source='strength')
fig.display() 