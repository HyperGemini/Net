import json
from os import path

def node_with_best_heuristic(open_set, heuristic_guess):
    result, min_path = None, float('inf')

    for v in open_set:
        hg = heuristic_guess[v]
        if hg < min_path:
            result = v
            min_path = hg

    return result


def h(n):
    H = {
            'Oradea': 380,
            'Zerind': 374,
            'Arad': 366,
            'Timisoara' : 329,
            'Lugoj' : 244,
            'Mehadia' : 241,
            'Drobeta' : 242,
            'Sibiu' : 253,
            'Fagaras': 176,
            'Rimnicu Vilacea' : 193,
            'Pitesti' : 100,
            'Craiova' : 160,
            'Buchares' : 0
    }

    return H[n] if n in H else 400


def astar(adj_list, start_node, target_node, h):
    # Otvoren skup cvorova
    open_set = set([start_node])

    parents = {}
    parents[start_node] = None

    shortset_paths = {v: float('inf') for v in adj_list}
    shortset_paths[start_node] = 0

    heuristic_guess = {v: float('inf') for v in adj_list}
    heuristic_guess[start_node] = 0

    path_found = False

    while len(open_set) > 0:
        current_node = node_with_best_heuristic(open_set, heuristic_guess)
        if current_node == target_node:
            path_found = True
            break

        open_set.remove(current_node)

        for (neighbour_node, weight) in adj_list[current_node]:
            new_path = shortset_paths[current_node] + weight
            if new_path < shortset_paths[neighbour_node]:
                parents[neighbour_node] = current_node
                shortset_paths[neighbour_node] = new_path
                heuristic_guess[neighbour_node] = new_path + h(neighbour_node) 
                if neighbour_node not in open_set:
                    open_set.add(neighbour_node)

    path = []
    if path_found:
        while target_node is not None:
            path.append(target_node)
            target_node = parents[target_node]
        path.reverse()
        
    return path                    


if __name__ == '__main__':
    with open('cities.json', 'r') as f:
        adj_list = dict(json.load(f))

    # print(adj_list)

    path = astar(adj_list, 'Arad', 'Buchares', h)
    print(path)