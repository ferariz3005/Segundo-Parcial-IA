import random

mex_tree_2 = [['CANCUN', [('VALLADOLID', 90), ('FELIPE CARRILLO PUERTO', 100)]],
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

# THIS IS THE HEURISTIC OF CABO SAN LUCAS
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


def Approved_n(neigh_list, tree):
    final_n = []

    for neighbor in neigh_list:
        current_node = neighbor[0]
        node_neighbors = [node_weights_list[1] for node_weights_list in tree if node_weights_list[0] == current_node]
        if len(node_neighbors) != 0:
            final_n.append(neighbor)

    return final_n


def Stochastic_Hill_Climber(tree, start, goal):
    nodes_visited = []
    branches = [[start]]
    visited_tuples = []

    while branches:

        print('----')
        print('\nBranches available: ', branches)
        branch = branches.pop()
        print('\nbranch to explore: ', branch)
        print('\nnodes visited: ', nodes_visited)

        current_node = branch[-1]
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

        for neighbors in node_neighbors:
            for neighbor in neighbors:
                value_h = h_sld_2[neighbor[0]]
                neighbors_with_h.append((neighbor[0], value_h))

        print(f"\nThis the the updated list (taking into account heuristic) of neighbors of node {current_node}: ",
              neighbors_with_h)

        neighbors_with_h = Approved_n(neighbors_with_h, tree)  # we make sure that
        print("\nThis is the list of approved neighbors (before): ", neighbors_with_h)

        for neighbor in neighbors_with_h:
            if neighbor in visited_tuples:
                neighbors_with_h.remove(neighbor)
        print("\nThis is the list of approved neighbors (after): ", neighbors_with_h)

        if len(neighbors_with_h) != 0:
            # the following piece of code turns our hill climber algorithm into a stochastic hill climbing search
            random_number = random.randint(0, len(neighbors_with_h) - 1)  # we obtain a random index
            key_tup = neighbors_with_h.pop(random_number)
            neighbors_with_h = [key_tup]
            print('\nThis is the neighbor to be explored:', neighbors_with_h)

            for neighbor in neighbors_with_h:
                print('\nCurrently exploring neighbor:', neighbor)
                if neighbor[0] == goal:  # *
                    branch.append(neighbor[0])
                    return branch

                if neighbor[0] not in nodes_visited:
                    updated_branch = branch.copy()
                    print('\nThis is the updated branch: ', updated_branch)
                    updated_branch.append(neighbor[0])
                    print('\nThis is the updated branch, having appended the neighbor: ', updated_branch)
                    branches.append(updated_branch)
                    print('\nThis is branches: ', branches)
        else:
            key_node = branch.pop(-1)
            key_tuple = (key_node, h_sld_2[key_node])
            visited_tuples.append(key_tuple)
            print('\nThis is the key_tuple: ', key_tuple)
            updated_branch = branch.copy()
            print('\nThis is branch after removing the faulty node: ', updated_branch)
            branches.append(updated_branch)
            print('\nThis is branches: ', branches)


def main():

    """start = input('\nstart node?: ')
    goal = input('\nstart node?: ')"""

    start = 'CANCUN'
    goal = 'ENSENADA'

    result = Stochastic_Hill_Climber(mex_tree_2, start, goal)
    print('\nThe path from {} to {} is {}\n'.format(start, goal, result))


main()
