from pyomo.environ import *

def create_model(nodes, demand, capacity, distance):

    model = ConcreteModel()

    trips = [1, 2]

    model.N = Set(initialize=nodes)
    model.C = Set(initialize=[i for i in nodes if i != 0])
    model.K = Set(initialize=trips)

    model.x = Var(model.N, model.N, model.K, domain=Binary)

    model.u = Var(model.C, model.K, bounds=(1, len(nodes)))

    def obj_rule(model):
        return sum(
            distance[i, j] * model.x[i, j, k]
            for i in model.N
            for j in model.N
            for k in model.K
        )

    model.obj = Objective(rule=obj_rule, sense=minimize)

    def visit_once_rule(model, c):
        return sum(
            model.x[i, c, k]
            for i in model.N if i != c
            for k in model.K
        ) == 1

    model.visit_once = Constraint(model.C, rule=visit_once_rule)

    def flow_rule(model, c, k):
        return (
            sum(model.x[i, c, k] for i in model.N if i != c)
            ==
            sum(model.x[c, j, k] for j in model.N if j != c)
        )

    model.flow = Constraint(model.C, model.K, rule=flow_rule)

    def start_rule(model, k):
        return sum(model.x[0, j, k] for j in model.C) == 1

    model.start = Constraint(model.K, rule=start_rule)

    def return_rule(model, k):
        return sum(model.x[i, 0, k] for i in model.C) == 1

    model.return_trip = Constraint(model.K, rule=return_rule)

    def capacity_rule(model, k):
        return sum(
            demand[c] *
            sum(
                model.x[i, c, k]
                for i in model.N if i != c
            )
            for c in model.C
        ) <= capacity

    model.capacity = Constraint(model.K, rule=capacity_rule)

    def self_loop_rule(model, i, k):
        return model.x[i, i, k] == 0

    model.self_loop = Constraint(
        model.N,
        model.K,
        rule=self_loop_rule
    )

    def subtour_rule(model, i, j, k):
        if i != j:
            return (
                model.u[i, k]
                - model.u[j, k]
                + len(model.C) * model.x[i, j, k]
                <= len(model.C) - 1
            )
        return Constraint.Skip

    model.subtour = Constraint(
        model.C,
        model.C,
        model.K,
        rule=subtour_rule
    )

    return model