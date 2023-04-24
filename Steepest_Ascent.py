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


def Steepest_Ascent_Hill_Climber(tree, start, goal):
    nodes_visited = []
    branches = [[start]]

    while branches:

        print('----')
        print('\nBranches available: ', branches)
        branch = branches.pop()
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

        current_h = h_sld[current_node]

        for node_weights_list in tree[1]:
            if node_weights_list[0] == current_node:
                while len(node_weights_list[1]) >= 1:  # we keep extracting neighbours as long as there's at least one
                    # neighbor
                    neigh = node_weights_list[1].pop()  # we opt to select the neighbor at the end
                    print(f'\nExploring neighbor: {neigh[0]}')
                    neigh_h = h_sld[neigh[0]]  # we get the neighbor's heuristic value
                    print(
                        f'\nThis is heuristic value of node {neigh[0]}: {neigh_h} vs the current heuristic: {current_h}')
                    if neigh_h < current_h:
                        branch.append(neigh[0])
                        if branch[-1] == goal:
                            return branch
                        else:
                            updated_branch = branch.copy()
                            print('\nThis is the updated branch, since a new maximum heuristic value has been found:',
                                  updated_branch)
                            branches.append(updated_branch)
                            print('\nThis is branches: ', branches)
                            break


def main():
    tree = generate_states(formed_graph)
    print('\ntree = ', tree[0], '\n')
    print('\ntree = ', tree[1], '\n')

    start = input('start node?: ')
    goal = "Bucharest"

    result = Steepest_Ascent_Hill_Climber(tree, start, goal)
    print('\nThe path from {} to {} is {}\n'.format(start, goal, result))


main()
