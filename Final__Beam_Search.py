
mex_tree_1 = [['CANCUN', [('VALLADOLID', 90), ('FELIPE CARRILLO PUERTO', 100)]],
              ['VALLADOLID', [('FELIPE CARRILLO PUERTO', 90)]], ['FELIPE CARRILLO PUERTO', [('CAMPECHE', 60)]],
              ['CAMPECHE', [('MERIDA', 90), ('CIUDAD DEL CARMEN', 90), ('CHETUMAL', 100)]],
              ['CIUDAD DEL CARMEN', [('VILLAHERMOSA', 90), ('TUXTLA', 90)]],
              ['CHETUMAL', [('FRANCISCO ESCARCEGA', 90)]], ['VILLAHERMOSA', [('ACAYUCAN', 90)]],
              ['TUXTLA', [('ACAYUCAN', 90)]], ['ACAYUCAN', [('TEHUANTEPEC', 80), ('ALVARADO', 110)]],
              ['ALVARADO', [('OAXACA', 100)]],
              ['OAXACA', [('PUERTO ANGEL', 90), ('IZUCAR DE MATAMOROS', 90), ('TEHUACAN', 80)]],
              ['PUERTO ANGEL', [('PINOTEPA NACIONAL', 100)]],
              ['IZUCAR DE MATAMOROS', [('CUERNAVACA', 100), ('PUEBLA', 90)]],
              ['PINOTEPA NACIONAL', [('ACAPULCO', 100)]],
              ['CUERNAVACA', [('CIUDAD DE MEXICO', 100), ('IGUALA', 100), ('CIUDAD ALTAMIRANO', 100)]],
              ['PUEBLA', [('CIUDAD DE MEXICO', 90), ('CORDOBA', 80)]], ['ACAPULCO', [('CHILPANCINGO', 140)]],
              ['CIUDAD DE MEXICO',
               [('TLAXCALA', 100), ('PACHUCA DE SOTO', 100), ('QUERETARO', 90), ('TOLUCA DE LERDO', 110)]],
              ['IGUALA', [('CIUDAD ALTAMIRANO', 110)]], ['CIUDAD ALTAMIRANO', [('ZIHUATANEJO', 90)]],
              ['CORDOBA', [('VERACRUZ', 90)]], ['CHILPANCINGO', [('IGUALA', 90)]],
              ['PACHUCA DE SOTO', [('TUXPAN DE RODRIGUEZ CANO', 110)]],
              ['QUERETARO', [('ATLACOMULCO', 90), ('SALAMANCA', 90), ('SAN LUIS POTOSI', 90)]],
              ['TOLUCA DE LERDO', [('CIUDAD ALTAMIRANO', 100)]], ['ZIHUATANEJO', [('PLAYA AZUL', 90)]],
              ['TUXPAN DE RODRIGUEZ CANO', [('TAMPICO', 80)]],
              ['SALAMANCA', [('GUANAJUATO', 90), ('MORELIA', 90), ('GUADALAJARA', 90)]],
              ['SAN LUIS POTOSI', [('AGUASCALIENTES', 100), ('ZACATECAS', 90), ('DURANGO', 70)]],
              ['PLAYA AZUL', [('COLIMA', 100), ('MANZANILLO', 100)]], ['TAMPICO', [('CIUDAD VICTORIA', 80)]],
              ['GUANAJUATO', [('AGUASCALIENTES', 80)]], ['GUADALAJARA', [('TEPIC', 110)]],
              ['AGUASCALIENTES', [('GUADALAJARA', 70)]], ['DURANGO', [('HIDALGO DEL PARRAL', 90), ('MAZATLAN', 90)]],
              ['COLIMA', [('GUADALAJARA', 50), ('MANZANILLO', 50)]], ['MANZANILLO', [('GUADALAJARA', 80)]],
              ['CIUDAD VICTORIA', [('DURANGO', 80), ('SOTO LA MARINA', 80), ('MATAMOROS', 80), ('MONTERREY', 80)]],
              ['TEPIC', [('MAZATLAN', 110)]],
              ['HIDALGO DEL PARRAL', [('CHIHUAHUA', 130), ('TOPOLOBAMPO', 110), ('CULIACAN', 80)]],
              ['MAZATLAN', [('CULIACAN', 90)]], ['MATAMOROS', [('REYNOSA', 90)]], ['MONTERREY', [('MONCLOVA', 70)]],
              ['CHIHUAHUA', [('CIUDAD JUAREZ', 90), ('JANOS', 90)]], ['TOPOLOBAMPO', [('CIUDAD OBREGON', 90)]],
              ['CULIACAN', [('TOPOLOBAMPO', 110)]], ['REYNOSA', [('NUEVO LAREDO', 90)]],
              ['MONCLOVA', [('TORREON', 110), ('OJINAGA', 110)]], ['JANOS', [('AGUA PRIETA', 110)]],
              ['CIUDAD OBREGON', [('GUAYMAS', 80)]], ['TORREON', [('DURANGO', 110)]], ['OJINAGA', [('CHIHUAHUA', 90)]],
              ['NUEVO LAREDO', [('MONTERREY', 110), ('PIEDRAS NEGRAS', 100)]], ['AGUA PRIETA', [('SANTA ANA', 110)]],
              ['GUAYMAS', [('HERMOSILLO', 80)]], ['PIEDRAS NEGRAS', [('MONCLOVA', 100)]],
              ['SANTA ANA', [('MEXICALI', 150)]], ['HERMOSILLO', [('SANTA ANA', 60)]],
              ['MEXICALI', [('TIJUANA', 110), ('SAN FELIPE', 70)]], ['TIJUANA', [('ENSENADA', 50)]],
              ['SAN FELIPE', [('ENSENADA', 50)]], ['ENSENADA', [('SAN QUINTIN', 60)]],
              ['SAN QUINTIN', [('SANTA ROSALIA', 60)]], ['SANTA ROSALIA', [('SANTO DOMINGO', 60)]],
              ['SANTO DOMINGO', [('LA PAZ', 70)]], ['LA PAZ', [('CABO SAN LUCAS', 70)]]]

h_sld_2 = {'CANCUN': 2381, 'VALLADOLID': 2256, 'FELIPE CARRILLO PUERTO': 2297, 'CAMPECHE': 2034, 'MERIDA': 2098,
           'CIUDAD DEL CARMEN': 1936, 'CHETUMAL': 2298, 'VILLAHERMOSA': 1849, 'TUXTLA': 1880,
           'FRANCISCO ESCARCEGA': 2045, 'ACAYUCAN': 1658, 'TEHUANTEPEC': 1701, 'ALVARADO': 1542, 'OAXACA': 1521,
           'PUERTO ANGEL': 1624, 'IZUCAR DE MATAMOROS': 1282, 'TEHUACAN': 1391, 'PINOTEPA NACIONAL': 1436,
           'CUERNAVACA': 1190, 'PUEBLA': 1287, 'ACAPULCO': 1245, 'CIUDAD DE MEXICO': 1130, 'IGUALA': 1193,
           'CIUDAD ALTAMIRANO': 1089, 'CORDOBA': 1419, 'CHILPANCINGO': 1239, 'TLAXCALA': 1254, 'PACHUCA DE SOTO': 1193,
           'QUERETARO': 1011, 'TOLUCA DE LERDO': 1140, 'ZIHUATANEJO': 1052, 'VERACRUZ': 1484,
           'TUXPAN DE RODRIGUEZ CANO': 1311, 'ATLACOMULCO': 1097, 'SALAMANCA': 939, 'SAN LUIS POTOSI': 921,
           'PLAYA AZUL': 961, 'TAMPICO': 1235, 'GUANAJUATO': 913, 'MORELIA': 966, 'GUADALAJARA': 720,
           'AGUASCALIENTES': 788, 'ZACATECAS': 751, 'DURANGO': 548, 'COLIMA': 760, 'MANZANILLO': 709,
           'CIUDAD VICTORIA': 1104, 'TEPIC': 542, 'HIDALGO DEL PARRAL': 614, 'MAZATLAN': 356, 'SOTO LA MARINA': 1202,
           'MATAMOROS': 1294, 'MONTERREY': 1011, 'CHIHUAHUA': 744, 'TOPOLOBAMPO': 314, 'CULIACAN': 328, 'REYNOSA': 1223,
           'MONCLOVA': 962, 'CIUDAD JUAREZ': 1029, 'JANOS': 906, 'CIUDAD OBREGON': 510, 'TORREON': 720, 'OJINAGA': 922,
           'NUEVO LAREDO': 1150, 'AGUA PRIETA': 937, 'GUAYMAS': 569, 'PIEDRAS NEGRAS': 1138, 'SANTA ANA': 858,
           'HERMOSILLO': 697, 'MEXICALI': 1211, 'TIJUANA': 1278, 'SAN FELIPE': 1026, 'ENSENADA': 1196,
           'SAN QUINTIN': 1041, 'SANTA ROSALIA': 547, 'SANTO DOMINGO': 343, 'LA PAZ': 142, 'CABO SAN LUCAS': 0}


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
            h_last_nodes.append((node, h_sld_2[node]))
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
        node_neighbors = [node_weights_list[1] for node_weights_list in tree if node_weights_list[0] == current_node]
        print(f"\nThese are the neighbors of node {current_node}: ", node_neighbors)

        for neighbor in node_neighbors[0]:  # itera en cada hijo
            value_h = h_sld_2[neighbor[0]]
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
            aux_with_h.append((node, h_sld_2[node]))

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
"""start = 'Arad'
goal = 'Bucharest'"""

start = 'CANCUN'
goal = 'CABO SAN LUCAS'
beam_width = 2

result = beam_search(mex_tree_1, start, goal, beam_width)
print('\nThe path from {} to {} is {} with a beam width of {}\n'.format(start, goal, result, beam_width))
