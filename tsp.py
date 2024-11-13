import itertools

heuristic_values = { 
    'A': {'B': 10, 'C': 15, 'D': 20},  
    'B': {'A': 10, 'C': 35, 'D': 25}, 
    'C': {'A': 15, 'B': 35, 'D': 30}, 
    'D': {'A': 20, 'B': 25, 'C': 30}
}

def find_optimal_route_and_cost(heuristic_values, start_city): 
    cities = list(heuristic_values.keys()) 
    cities.remove(start_city) 
    min_cost = float('inf') 
    best_route = None 
    all_routes = [] 

    for perm in itertools.permutations(cities): 
        route = [start_city] + list(perm) + [start_city] 
        total_cost = 0 
        for i in range(len(route) - 1): 
            total_cost += heuristic_values[route[i]][route[i + 1]] 
        all_routes.append((route, total_cost)) 
        if total_cost < min_cost: 
            min_cost = total_cost 
            best_route = route

    return best_route, min_cost, all_routes

start_city = 'A'
route, total_cost, all_routes = find_optimal_route_and_cost(heuristic_values, start_city)
print("Optimal Route:", route)
print("Minimum Cost:", total_cost)
