import json
import codecs
from queue import Queue

# adj_list - lista suseda
# start_node - pocetni cvor
# traversal - pronadjeni put
# visited - poseceni cvorovi

def depth_first_traversal(adj_list, start_node, traversal, visited = set()):
    if start_node in visited:
        return
    visited.add(start_node)
    traversal.append(start_node)

    for (next_city, distance) in adj_list[start_node]:
        if next_city not in visited:
            depth_first_traversal(adj_list, next_city, traversal, visited)


def depth_first_search(adj_list, start_node, target_node, path, visited = set()):
    path.append(start_node)
    if start_node == target_node:
        return path
    visited.add(start_node)

    for (next_city, distance) in adj_list[start_node]:
        if next_city not in visited:
            result = depth_first_search(adj_list, next_city, target_node, path, visited)
            if result is not None:
                return result

    path.pop()
    return None


def breadth_first_search(adj_list, start_node, target_node):
    visited = set()
    queue = Queue()
    queue.put(start_node)
    visited.add(start_node)

    parent = dict()
    parent[start_node] = None
    path_found = False

    while not queue.empty():
        current_node = queue.get()
        if current_node == target_node:
            path_found = True
            break

        for (next_node, distance) in adj_list[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)

    path = []
    if path_found:
        path.append(target_node)
        while True:
            parent_node = parent[target_node]
            if parent_node is None:
                break
            path.append(parent_node)
            target_node = parent_node
        path.reverse()
    return path


if __name__ == '__main__':
    with codecs.open('cities.json', 'r', 'utf-8') as f:
        adj_list = json.load(f)
        

    # print("DEPTH FIRST TRAVERSAL")
    # traversal = []

    # depth_first_traversal(adj_list, 'Oradea', traversal)
    # print(traversal)

    # print("DEPTH FIRST SEARCH")
    # path = []

    # depth_first_search(adj_list, 'Drobeta', 'Lugoj', path)
    # print(path)

    print('BREADTH FIRST SEARCH')
    path = breadth_first_search(adj_list, 'Drobeta', 'Lugoj')
    print(path)