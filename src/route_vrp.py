"""
Route Optimization Module (VRP)
RPM Hire Hackathon Prototype
"""

# === Mock Version (quick demo, always works) ===
def optimize_route(use_mock=True):
    """
    Optimize equipment delivery route.
    - If use_mock=True: returns a fixed sample route (fast, guaranteed to run)
    - If use_mock=False: runs OR-Tools solver for actual optimization
    """
    if use_mock:
        # Simple fixed route (safe fallback)
        route = ["Warehouse_Melbourne", "Project_A", "Project_B", "Warehouse_Melbourne"]
        return route
    else:
        try:
            # Try OR-Tools solver version
            return optimize_route_ortools()
        except Exception as e:
            print("⚠️ OR-Tools solver failed, fallback to mock route. Error:", e)
            return ["Warehouse_Melbourne", "Project_A", "Project_B", "Warehouse_Melbourne"]


# === OR-Tools Version (real VRP solver) ===
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def optimize_route_ortools():
    """
    Use OR-Tools to solve a simple Vehicle Routing Problem (VRP).
    Returns a list of nodes visited in optimal order.
    """

    # Mock distance matrix (Depot + 3 sites)
    distance_matrix = [
        [0, 20, 40, 25],
        [20, 0, 15, 30],
        [40, 15, 0, 10],
        [25, 30, 10, 0],
    ]
    depot = 0
    num_vehicles = 1

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_vehicles, depot)

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        return distance_matrix[manager.IndexToNode(from_index)][manager.IndexToNode(to_index)]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Set search parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve
    solution = routing.SolveWithParameters(search_parameters)
    if not solution:
        raise RuntimeError("No solution found by OR-Tools")

    # Extract route
    route = []
    index = routing.Start(0)
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    route.append(manager.IndexToNode(index))

    return route


# === Debug/Test Run ===
if __name__ == "__main__":
    print("Mock Route:", optimize_route(use_mock=True))
    print("OR-Tools Route:", optimize_route(use_mock=False))

