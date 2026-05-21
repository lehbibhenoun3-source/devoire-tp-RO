def print_solution(routing, manager, solution, data):

    if not solution:
        print("Pas de solution")
        return

    total = 0
    routes = []

    print("\n===== PLAN =====")

    for v in range(data["num_vehicles"]):

        index = routing.Start(v)

        route = []
        load = 0
        dist = 0

        while not routing.IsEnd(index):

            node = manager.IndexToNode(index)
            route.append(node)

            load += data["demands"][node]

            prev = index
            index = solution.Value(routing.NextVar(index))

            dist += routing.GetArcCostForVehicle(prev, index, v)

        route.append(manager.IndexToNode(index))

        print(f"\nCamion {v+1}")
        print(" -> ".join([data["names"][i] for i in route]))
        print("Charge:", load)
        print("Distance:", dist)

        total += dist
        routes.append(route)

    print("\nTotal:", total)

    return routes