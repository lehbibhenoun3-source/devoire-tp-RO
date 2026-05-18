from itertools import permutations
from donnees import demande, distance

clients_trajet1 = [1, 2, 4]
clients_trajet2 = [3, 5, 6]


def meilleur_trajet(clients):
    meilleur_cout = float("inf")
    meilleur_chemin = None

    for permutation_clients in permutations(clients):

        trajet = [0] + list(permutation_clients) + [0]

        cout = 0

        for i in range(len(trajet) - 1):
            cout += distance[
                (trajet[i], trajet[i + 1])
            ]

        if cout < meilleur_cout:
            meilleur_cout = cout
            meilleur_chemin = trajet

    return meilleur_chemin, meilleur_cout


trajet1, cout1 = meilleur_trajet(clients_trajet1)
trajet2, cout2 = meilleur_trajet(clients_trajet2)

print("===== TRAJETS FINAUX =====")

print(
    "Trajet 1 :",
    " → ".join(map(str, trajet1))
)
print("Distance :", cout1, "km")

print()

print(
    "Trajet 2 :",
    " → ".join(map(str, trajet2))
)
print("Distance :", cout2, "km")

print()
print(
    "Distance totale =",
    cout1 + cout2,
    "km"
)