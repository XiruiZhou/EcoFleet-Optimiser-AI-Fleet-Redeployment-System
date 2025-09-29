# src/route_vrp.py
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

def create_data_model():
    return {
        "distance_matrix": [
            [0, 20, 18, 30],
            [20, 0, 25, 35],
            [18, 25, 0, 15],
            [30, 35, 15, 0],
        ],
        "num_vehicles": 1,
        "depot": 0
    }

def solve_vrp():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data["distance_matrix"]), data["num_vehicles"], data["depot"])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        return data["distance_matrix"][manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        route = []
        index = routing.Start(0)
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))
        return route
    return None

if __name__ == "__main__":
    print("Optimal route:", solve_vrp())
