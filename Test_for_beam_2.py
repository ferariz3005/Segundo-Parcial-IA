formed_graph = [
    [0, 118, 140, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 80, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 71, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 146, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 211, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 138, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 85, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 98, 142, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 92, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

h_sld = {
    'Arad': 366,
    'Timisoara': 329,
    'Sibiu': 253,
    'Zerind': 374,
    'Lugoj': 244,
    'Rimnicu Vilcea': 193,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Urziceni': 80,
    'Vaslui': 199,
}


def generate_states(graph):
    nodes_tuples = []
    nodes_connection_weights = []
    available_nodes_names = ['Arad', 'Timisoara', 'Sibiu', 'Zerind', 'Lugoj', 'Rimnicu Vilcea', 'Fagaras', 'Oradea',
                             'Mehadia', 'Craiova', 'Pitesti', 'Bucharest', 'Drobeta', 'Giurgiu', 'Urziceni', 'Hirsova',
                             'Vaslui', 'Efoire', 'Iasi', 'Neamt']
    for matrix_row_index in range(len(graph)):
        # print('matrix row' , graph[matrix_row_index])
        connections_and_weights = []
        for matrix_column_index in range(len(graph[0])):
            if graph[matrix_row_index][matrix_column_index] != 0:
                nodes_tuples.append(
                    (available_nodes_names[matrix_row_index], available_nodes_names[matrix_column_index]))
                connections_and_weights.append(
                    (available_nodes_names[matrix_column_index], graph[matrix_row_index][matrix_column_index]))
        if len(connections_and_weights) != 0:
            nodes_connection_weights.append([available_nodes_names[matrix_row_index], connections_and_weights])
    return nodes_tuples, nodes_connection_weights


def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup


def beam_search(tree, start, goal, beam_width):
    global branch
    nodes_visited = []
    branches = [[start]]

    while branches:
        #  this piece of code ensures that we always take the lowest heuristic value node
        last_nodes = [path[-1] for path in
                      branches]  # we create a list with the last nodes of all of our possible paths
        print('\nThese are the last nodes from all possible paths:', last_nodes)
        h_last_nodes = []
        for node in last_nodes:
            h_last_nodes.append((node, h_sld[node]))
        print('\nThis is h_last_nodes list:', h_last_nodes)
        lowest_h_value = min(h_last_nodes)
        print('\nThis is the lowest value from h_las_nodes list:', lowest_h_value)
        key_node = lowest_h_value[0]

        for path in branches:
            if key_node == path[-1]:
                branch = path
                branches.remove(path)
                break

        print('----')
        print('\nBranches available: ', branches)
        print('\nbranch to explore: ', branch)
        print('\nnodes visited: ', nodes_visited)

        current_node = branch[-1]  # we take the last node of our possible path as our current node
        print('\ncurrent node ', current_node)

        # checks if the node where we are located is the stop
        if current_node == goal:
            return branch

        if current_node not in nodes_visited:
            nodes_visited.append(current_node)
        print('\nThese are the nodes that have been visited:', nodes_visited)

        neighbors_with_h = []
        # we get the neighbors of every node as we did in greedy
        node_neighbors = [node_weights_list[1] for node_weights_list in tree[1] if node_weights_list[0] == current_node]
        print(f"\nThese are the neighbors of node {current_node}: ", node_neighbors)

        for neighbor in node_neighbors[0]:  # itera en cada hijo
            value_h = h_sld[neighbor[0]]
            neighbors_with_h.append((neighbor[0], value_h))
        print(f"\nThis the the updated list (taking into account heuristic) of neighbors of node {current_node}: ",
              neighbors_with_h)

        sorted_neighbors = Sort_Tuple(neighbors_with_h)
        print(f"\nThis is the sorted list of neighbors of node {current_node}: {sorted_neighbors}")

        for neighbor in sorted_neighbors[0:beam_width]:  # *******
            print('\nCurrently exploring neighbor:', neighbor[0])
            if neighbor[0] == goal:
                branch.append(neighbor[0])
                return branch

            if neighbor[0] not in nodes_visited:
                updated_branch = branch.copy()
                print('\nThis is the updated branch: ', updated_branch)
                updated_branch.append(neighbor[0])
                print('\nThis is the updated branch, having appended the neighbor: ', updated_branch)
                branches.append(updated_branch)
                print('\nThis is branches: ', branches)
                
        # *********************************************************************************************************
        print("\nThis is 'branches' before restricting it to beam_width :", branches)
        aux = [possible_path[-1] for possible_path in
               branches]  # we create a list with the last nodes of all of our possible paths
        print('\nThese are the last nodes from all possible paths:', aux)

        aux_with_h = []
        for node in aux:
            aux_with_h.append((node, h_sld[node]))

        print('\nThis is aux_with_h list:', aux_with_h)
        sorted_aux_list = Sort_Tuple(aux_with_h)
        print(f"\nFirst we sort our list: {sorted_aux_list}")

        cool_list = sorted_aux_list[0:beam_width]  # we restrict the number of paths to be explored
        aux_2 = []
        for tup in cool_list:
            aux_2.append(tup[0])
        print(f"\nThis is the nodes we're interested in, since they've got the lowest heuristic values: {aux_2}")
        for path in branches:
            if path[-1] not in aux_2:
                branches.remove(path)

        print("\nThis is 'branches' after being restricted by beam_width:", branches)


tree = generate_states(formed_graph)
start = 'Arad'
goal = 'Bucharest'
beam_width = 2

result = beam_search(tree, start, goal, beam_width)
print('\nThe path from {} to {} is {} with a beam width of {}\n'.format(start, goal, result, beam_width))
