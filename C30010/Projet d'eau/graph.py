import networkx as nx
import matplotlib.pyplot as plt

from solve import routes
from donnees import nodes

G = nx.DiGraph()

for node in nodes:
    G.add_node(node)

colors_list = ['blue', 'red']

for k, route in routes.items():
    color = colors_list[k-1]

    for i in range(len(route)-1):
        G.add_edge(
            route[i],
            route[i+1],
            color=color
        )

pos = {
    0: (0,0),
    1: (2,3),
    2: (4,4),
    3: (6,2),
    4: (3,-2),
    5: (7,-1),
    6: (9,2)
}

colors = [G[u][v]['color'] for u,v in G.edges()]

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500,
    node_color='skyblue',
    edge_color=colors,
    width=3,
    arrows=True
)

plt.title("Optimal Routes")
plt.savefig("water_routes.png")

print("Graph saved successfully!")