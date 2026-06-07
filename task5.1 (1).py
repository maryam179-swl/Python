# Romania Map Graph (without distances for IDS)
romania_map = {
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

# -------------------------------
# Depth-Limited Search (DLS)
# -------------------------------
def depth_limited_search(start, goal, limit, path, visited):
    path.append(start)
    visited.add(start)

    if start == goal:
        return path

    if limit <= 0:
        path.pop()
        return None

    for neighbor in romania_map[start]:
        if neighbor not in visited:
            result = depth_limited_search(neighbor, goal, limit - 1, path, visited)
            if result:
                return result

    path.pop()
    return None

# -------------------------------
# Iterative Deepening Search (IDS)
# -------------------------------
def iterative_deepening_search(start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = []
        result = depth_limited_search(start, goal, depth, path, visited)
        if result:
            return result
    return None


# Run IDS from Arad → Bucharest
start_city = 'Arad'
goal_city = 'Bucharest'
max_depth = 10   # safe limit

path = iterative_deepening_search(start_city, goal_city, max_depth)

if path:
    print("Path found (Arad → Bucharest):", " -> ".join(path))
else:
    print("No path found within depth limit.")