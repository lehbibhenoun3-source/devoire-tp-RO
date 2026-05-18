import networkx as nx
import matplotlib.pyplot as plt
from donnees import noeuds
from solve import trajet1, trajet2   # <-- important

G = nx.DiGraph()

for noeud in noeuds:
    G.add_node(noeud)

for i in range(len(trajet1)-1):
    G.add_edge(
        trajet1[i],
        trajet1[i+1],
        color="blue"
    )

for i in range(len(trajet2)-1):
    G.add_edge(
        trajet2[i],
        trajet2[i+1],
        color="red"
    )

positions = {
    0: (0,0),
    1: (2,3),
    2: (4,4),
    3: (6,2),
    4: (3,-2),
    5: (7,-1),
    6: (9,2)
}

couleurs = [
    G[u][v]["color"]
    for u, v in G.edges()
]

etiquettes = {
    0: "Dépôt",
    1: "Client 1",
    2: "Client 2",
    3: "Client 3",
    4: "Client 4",
    5: "Client 5",
    6: "Client 6"
}

nx.draw(
    G,
    positions,
    labels=etiquettes,
    with_labels=True,
    node_size=2500,
    node_color="skyblue",
    edge_color=couleurs,
    width=3,
    arrows=True
)

plt.title("Routes réellement utilisées")
plt.savefig("routes_reelles.png")
plt.show()