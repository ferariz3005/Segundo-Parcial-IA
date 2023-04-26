# DIRECTED TREE
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
# UNIDIRECTIONAL TREE
mex_tree_2 = [['CANCUN', [('VALLADOLID', 90), ('FELIPE CARRILLO PUERTO', 100)]],
              ['VALLADOLID', [('CANCUN', 90), ('FELIPE CARRILLO PUERTO', 90)]],
              ['FELIPE CARRILLO PUERTO', [('CANCUN', 100), ('VALLADOLID', 90), ('CAMPECHE', 60)]], ['CAMPECHE', [
        ('FELIPE CARRILLO PUERTO', 60), ('MERIDA', 90), ('CIUDAD DEL CARMEN', 90), ('CHETUMAL', 100)]],
              ['MERIDA', [('CAMPECHE', 90)]],
              ['CIUDAD DEL CARMEN', [('CAMPECHE', 90), ('VILLAHERMOSA', 90), ('TUXTLA', 90)]],
              ['CHETUMAL', [('CAMPECHE', 100), ('FRANCISCO ESCARCEGA', 90)]],
              ['VILLAHERMOSA', [('CIUDAD DEL CARMEN', 90), ('ACAYUCAN', 90)]],
              ['TUXTLA', [('CIUDAD DEL CARMEN', 90), ('ACAYUCAN', 90)]], ['FRANCISCO ESCARCEGA', [('CHETUMAL', 90)]],
              ['ACAYUCAN', [('VILLAHERMOSA', 90), ('TUXTLA', 90), ('TEHUANTEPEC', 80), ('ALVARADO', 110)]],
              ['TEHUANTEPEC', [('ACAYUCAN', 80)]], ['ALVARADO', [('ACAYUCAN', 110), ('OAXACA', 100)]],
              ['OAXACA', [('ALVARADO', 100), ('PUERTO ANGEL', 90), ('IZUCAR DE MATAMOROS', 90), ('TEHUACAN', 80)]],
              ['PUERTO ANGEL', [('OAXACA', 90), ('PINOTEPA NACIONAL', 100)]],
              ['IZUCAR DE MATAMOROS', [('OAXACA', 90), ('CUERNAVACA', 100), ('PUEBLA', 90)]],
              ['TEHUACAN', [('OAXACA', 80)]], ['PINOTEPA NACIONAL', [('PUERTO ANGEL', 100), ('ACAPULCO', 100)]],
              ['CUERNAVACA',
               [('IZUCAR DE MATAMOROS', 100), ('CIUDAD DE MEXICO', 100), ('IGUALA', 100), ('CIUDAD ALTAMIRANO', 100)]],
              ['PUEBLA', [('IZUCAR DE MATAMOROS', 90), ('CIUDAD DE MEXICO', 90), ('CORDOBA', 80)]],
              ['ACAPULCO', [('PINOTEPA NACIONAL', 100), ('CHILPANCINGO', 140)]], ['CIUDAD DE MEXICO',
                                                                                  [('CUERNAVACA', 100), ('PUEBLA', 90),
                                                                                   ('TLAXCALA', 100),
                                                                                   ('PACHUCA DE SOTO', 100),
                                                                                   ('QUERETARO', 90),
                                                                                   ('TOLUCA DE LERDO', 110)]],
              ['IGUALA', [('CUERNAVACA', 100), ('CIUDAD ALTAMIRANO', 110), ('CHILPANCINGO', 90)]], ['CIUDAD ALTAMIRANO',
                                                                                                    [(
                                                                                                        'CUERNAVACA',
                                                                                                        100),
                                                                                                        ('IGUALA', 110),
                                                                                                        (
                                                                                                            'TOLUCA DE LERDO',
                                                                                                            100), (
                                                                                                        'ZIHUATANEJO',
                                                                                                        90)]],
              ['CORDOBA', [('PUEBLA', 80), ('VERACRUZ', 90)]], ['CHILPANCINGO', [('ACAPULCO', 140), ('IGUALA', 90)]],
              ['TLAXCALA', [('CIUDAD DE MEXICO', 100)]],
              ['PACHUCA DE SOTO', [('CIUDAD DE MEXICO', 100), ('TUXPAN DE RODRIGUEZ CANO', 110)]], ['QUERETARO', [
        ('CIUDAD DE MEXICO', 90), ('ATLACOMULCO', 90), ('SALAMANCA', 90), ('SAN LUIS POTOSI', 90)]],
              ['TOLUCA DE LERDO', [('CIUDAD DE MEXICO', 110), ('CIUDAD ALTAMIRANO', 100)]],
              ['ZIHUATANEJO', [('CIUDAD ALTAMIRANO', 90), ('PLAYA AZUL', 90)]], ['VERACRUZ', [('CORDOBA', 90)]],
              ['TUXPAN DE RODRIGUEZ CANO', [('PACHUCA DE SOTO', 110), ('TAMPICO', 80)]],
              ['ATLACOMULCO', [('QUERETARO', 90)]],
              ['SALAMANCA', [('QUERETARO', 90), ('GUANAJUATO', 90), ('MORELIA', 90), ('GUADALAJARA', 90)]],
              ['SAN LUIS POTOSI', [('QUERETARO', 90), ('AGUASCALIENTES', 100), ('ZACATECAS', 90), ('DURANGO', 70)]],
              ['PLAYA AZUL', [('ZIHUATANEJO', 90), ('COLIMA', 100), ('MANZANILLO', 100)]],
              ['TAMPICO', [('TUXPAN DE RODRIGUEZ CANO', 80), ('CIUDAD VICTORIA', 80)]],
              ['GUANAJUATO', [('SALAMANCA', 90), ('AGUASCALIENTES', 80)]], ['MORELIA', [('SALAMANCA', 90)]],
              ['GUADALAJARA',
               [('SALAMANCA', 90), ('AGUASCALIENTES', 70), ('COLIMA', 50), ('MANZANILLO', 80), ('TEPIC', 110)]],
              ['AGUASCALIENTES', [('SAN LUIS POTOSI', 100), ('GUANAJUATO', 80), ('GUADALAJARA', 70)]],
              ['ZACATECAS', [('SAN LUIS POTOSI', 90)]], ['DURANGO', [('SAN LUIS POTOSI', 70), ('CIUDAD VICTORIA', 80),
                                                                     ('HIDALGO DEL PARRAL', 90), ('MAZATLAN', 90),
                                                                     ('TORREON', 110)]],
              ['COLIMA', [('PLAYA AZUL', 100), ('GUADALAJARA', 50), ('MANZANILLO', 50)]],
              ['MANZANILLO', [('PLAYA AZUL', 100), ('GUADALAJARA', 80), ('COLIMA', 50)]], ['CIUDAD VICTORIA',
                                                                                           [('TAMPICO', 80),
                                                                                            ('DURANGO', 80),
                                                                                            ('SOTO LA MARINA', 80),
                                                                                            ('MATAMOROS', 80),
                                                                                            ('MONTERREY', 80)]],
              ['TEPIC', [('GUADALAJARA', 110), ('MAZATLAN', 110)]],
              ['HIDALGO DEL PARRAL', [('DURANGO', 90), ('CHIHUAHUA', 130), ('TOPOLOBAMPO', 110), ('CULIACAN', 80)]],
              ['MAZATLAN', [('DURANGO', 90), ('TEPIC', 110), ('CULIACAN', 90)]],
              ['SOTO LA MARINA', [('CIUDAD VICTORIA', 80)]], ['MATAMOROS', [('CIUDAD VICTORIA', 80), ('REYNOSA', 90)]],
              ['MONTERREY', [('CIUDAD VICTORIA', 80), ('MONCLOVA', 70), ('NUEVO LAREDO', 110)]],
              ['CHIHUAHUA', [('HIDALGO DEL PARRAL', 130), ('CIUDAD JUAREZ', 90), ('JANOS', 90), ('OJINAGA', 90)]],
              ['TOPOLOBAMPO', [('HIDALGO DEL PARRAL', 110), ('CULIACAN', 110), ('CIUDAD OBREGON', 90)]],
              ['CULIACAN', [('HIDALGO DEL PARRAL', 80), ('MAZATLAN', 90), ('TOPOLOBAMPO', 110)]],
              ['REYNOSA', [('MATAMOROS', 90), ('NUEVO LAREDO', 90)]],
              ['MONCLOVA', [('MONTERREY', 70), ('TORREON', 110), ('OJINAGA', 110), ('PIEDRAS NEGRAS', 100)]],
              ['CIUDAD JUAREZ', [('CHIHUAHUA', 90)]], ['JANOS', [('CHIHUAHUA', 90), ('AGUA PRIETA', 110)]],
              ['CIUDAD OBREGON', [('TOPOLOBAMPO', 90), ('GUAYMAS', 80)]],
              ['TORREON', [('DURANGO', 110), ('MONCLOVA', 110)]], ['OJINAGA', [('CHIHUAHUA', 90), ('MONCLOVA', 110)]],
              ['NUEVO LAREDO', [('MONTERREY', 110), ('REYNOSA', 90), ('PIEDRAS NEGRAS', 100)]],
              ['AGUA PRIETA', [('JANOS', 110), ('SANTA ANA', 110)]],
              ['GUAYMAS', [('CIUDAD OBREGON', 80), ('HERMOSILLO', 80)]],
              ['PIEDRAS NEGRAS', [('MONCLOVA', 100), ('NUEVO LAREDO', 100)]],
              ['SANTA ANA', [('AGUA PRIETA', 110), ('HERMOSILLO', 60), ('MEXICALI', 150)]],
              ['HERMOSILLO', [('GUAYMAS', 80), ('SANTA ANA', 60)]],
              ['MEXICALI', [('SANTA ANA', 150), ('TIJUANA', 110), ('SAN FELIPE', 70)]],
              ['TIJUANA', [('MEXICALI', 110), ('ENSENADA', 50)]], ['SAN FELIPE', [('MEXICALI', 70), ('ENSENADA', 50)]],
              ['ENSENADA', [('TIJUANA', 50), ('SAN FELIPE', 50), ('SAN QUINTIN', 60)]],
              ['SAN QUINTIN', [('ENSENADA', 60), ('SANTA ROSALIA', 60)]],
              ['SANTA ROSALIA', [('SAN QUINTIN', 60), ('SANTO DOMINGO', 60)]],
              ['SANTO DOMINGO', [('SANTA ROSALIA', 60), ('LA PAZ', 70)]],
              ['LA PAZ', [('SANTO DOMINGO', 70), ('CABO SAN LUCAS', 70)]], ['CABO SAN LUCAS', [('LA PAZ', 70)]]]
# THIS IS THE HEURISTIC FOR CABO SAN LUCAS

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


# This is a list of all cities which do not possess any neighbors
banned_nodes = ['MERIDA', 'FRANCISCO ESCARCEGA', 'TEHUANTEPEC', 'TEHUACAN', 'IGUALA', 'TLAXCALA', 'VERACRUZ',
                'ATLACOMULCO', 'MORELIA', 'ZACATECAS', 'SOTO LA MARINA', 'CIUDAD JUAREZ', 'SANTA ANA', 'CABO SAN LUCAS']


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

        current_h = h_sld_2[current_node]

        for node_weights_list in tree:
            if node_weights_list[0] == current_node:
                print(f'\nThese are the neighbors of node {current_node}: {node_weights_list[1]}')
                while len(node_weights_list[1]) >= 1:  # we keep extracting neighbours as long as there's at least one
                    # neighbor
                    print(f'\nThis is the list of neighbors of node {current_node}:', node_weights_list[1])
                    neighbor = node_weights_list[1].pop()  # we opt to select the neighbor at the end
                    if neighbor[0] in banned_nodes: # if our initial choice of neighbor happens to be in the list of
                        # banned cities, we pick another one (if available)
                        if len(node_weights_list[1]) >= 1:
                            neighbor = node_weights_list[1].pop()
                        else:
                            return "none since the last reached state has no more neighbors"
                    print(f'\nExploring neighbor: {neighbor}')
                    neighbor_h = h_sld_2[neighbor[0]]  # we get the neighbor's heuristic value
                    print(
                        f'\nThis is heuristic value of node {neighbor[0]}: {neighbor_h} vs the current heuristic: {current_h}')
                    if neighbor_h < current_h:
                        branch.append(neighbor[0])
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

    """start = input('start node?: ')
    goal = input('start node?: ')"""

    start = 'CANCUN'
    goal = 'CABO SAN LUCAS'

    result = Steepest_Ascent_Hill_Climber(mex_tree_1, start, goal)
    print('\nThe path from {} to {} is {}\n'.format(start, goal, result))


main()
