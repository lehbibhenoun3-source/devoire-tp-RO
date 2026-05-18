from pyomo.environ import value
from pyomo.opt import SolverFactory

from model import create_model
from donnees import nodes, demand, truck_capacity, distance

model = create_model(
    nodes,
    demand,
    truck_capacity,
    distance
)

solver = SolverFactory("highs")
solver.solve(model)

routes = {}

print("===== FINAL ROUTES =====")

total_distance = 0

for k in model.K:
    route = [0]
    current = 0

    while True:
        next_node = None

        for j in model.N:
            if j != current and value(model.x[current, j, k]) == 1:
                next_node = j
                break

        if next_node is None:
            break

        route.append(next_node)

        if next_node == 0:
            break

        current = next_node

    if len(route) > 2:
        routes[k] = route

        cost = 0
        for i in range(len(route)-1):
            cost += distance[(route[i], route[i+1])]

        total_distance += cost

        print(
            f"Trip {k}:",
            " → ".join(map(str, route))
        )
        print(f"Distance: {cost} km")
        print()

print(f"Total Distance = {total_distance} km")