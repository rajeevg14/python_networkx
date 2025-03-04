import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

df = pd.DataFrame({'id1': {0: 'a1', 1: 'a1', 2: 'a1', 3: 'b2', 4: 'c1'},
                   'id2': {0: 'b1', 1: 'b2', 2: 'c1', 3: 'c1', 4: 'a1'},
                   'val': {0: 10, 1: 4, 2: 1, 3: 15, 4: 3}})

g = nx.from_pandas_edgelist(df, source="id1", target="id2")

d = df.groupby("id2")["val"].sum().to_dict()
for node in g.nodes:
    d.setdefault(node, 1)

nodes, values = zip(*d.items())
nx.draw(g, nodelist=list(nodes), node_size=[v * 100 for v in values], with_labels=True)
plt.show()