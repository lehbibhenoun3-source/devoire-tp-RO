from data.data import *
from solver.solver import solve_vrp
from utils.printer import print_solution
from utils.graph import plot_routes

data = {
    "distance_matrix": distance_matrix,
    "names": names,
    "demands": demands,
    "capacity": capacity,
    "num_vehicles": num_vehicles,
    "depot": depot
}

routing, manager, solution = solve_vrp(
    distance_matrix,
    demands,
    capacity,
    num_vehicles,
    depot
)

routes = print_solution(routing, manager, solution, data)

if routes:
    plot_routes(routes, coords, names)