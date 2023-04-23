import math
from math import radians, cos, sin, asin, sqrt

cities_coordinates = {
    'CANCUN': (21.1213285, -86.9192738)
    , 'VALLADOLID': (20.688114, -88.2204456)
    , 'FELIPE CARRILLO PUERTO': (19.5778903, -88.0630853)
    , 'CAMPECHE': (19.8305682, -90.5798365)
    , 'MERIDA': (20.9800512, -89.7029587)
    , 'CIUDAD DEL CARMEN': (18.6118375, -91.8927345)
    , 'CHETUMAL': (18.5221567, -88.3397982)
    , 'VILLAHERMOSA': (17.9925264, -92.9881407)
    , 'TUXTLA': (16.7459857, -93.1996103)
    , 'FRANCISCO ESCARCEGA': (18.6061556, -90.8176486)
    , 'ACAYUCAN': (17.951096, -94.9306961)
    , 'TEHUANTEPEC': (16.320636, -95.27521)
    , 'ALVARADO': (18.7760455, -95.7731952)
    , 'OAXACA': (17.0812951, -96.7707511)
    , 'PUERTO ANGEL': (15.6679974, -96.4933733)
    , 'IZUCAR DE MATAMOROS': (18.5980563, -98.5076767)
    , 'TEHUACAN': (18.462191, -97.4437333)
    , 'PINOTEPA NACIONAL': (16.3442895, -98.1315923)
    , 'CUERNAVACA': (18.9318685, -99.3106054)
    , 'PUEBLA': (19.040034, -98.2630056)
    , 'ACAPULCO': (16.8354485, -99.9323491)
    , 'CIUDAD DE MEXICO': (19.3898319, -99.7180148)
    , 'IGUALA': (18.3444, -99.5652232)
    , 'CIUDAD ALTAMIRANO': (18.3547491, -100.6817619)
    , 'CORDOBA': (18.8901707, -96.9751108)
    , 'CHILPANCINGO': (17.5477072, -99.5324349)
    , 'TLAXCALA': (19.4167798, -98.4471127)
    , 'PACHUCA DE SOTO': (20.0825056, -98.8268184)
    , 'QUERETARO': (20.6121228, -100.4802576)
    , 'TOLUCA DE LERDO': (19.294109, -99.6662331)
    , 'ZIHUATANEJO': (17.6405745, -101.5601369)
    , 'VERACRUZ': (19.1787635, -96.2113357)
    , 'TUXPAN DE RODRIGUEZ CANO': (20.9596561, -97.4158767)
    , 'ATLACOMULCO': (19.7980152, -99.89317)
    , 'SALAMANCA': (20.5664927, -101.2176511)
    , 'SAN LUIS POTOSI': (22.1127046, -101.0261099)
    , 'PLAYA AZUL': (17.9842581, -102.357616)
    , 'TAMPICO': (22.2662251, -97.939526)
    , 'GUANAJUATO': (21.0250928, -101.3296402)
    , 'MORELIA': (19.7036417, -101.2761644)
    , 'GUADALAJARA': (20.6737777, -103.4054536)
    , 'AGUASCALIENTES': (21.8857199, -102.36134)
    , 'ZACATECAS': (22.7636293, -102.623638)
    , 'DURANGO': (24.0226824, -104.7177652)
    , 'COLIMA': (19.2400444, -103.7636273)
    , 'MANZANILLO': (19.0775491, -104.4789574)
    , 'CIUDAD VICTORIA': (23.7409928, -99.1783576)
    , 'TEPIC': (21.5009822, -104.9119242)
    , 'HIDALGO DEL PARRAL': (26.9489283, -105.8211168)
    , 'MAZATLAN': (23.2467283, -106.4923175)
    , 'SOTO LA MARINA': (23.7673729, -98.2157573)
    , 'MATAMOROS': (25.8433787, -97.5849847)
    , 'MONTERREY': (25.6487281, -100.4431819)
    , 'CHIHUAHUA': (28.6708592, -106.2047036)
    , 'TOPOLOBAMPO': (25.6012747, -109.0687891)
    , 'CULIACAN': (24.8049008, -107.4933545)
    , 'REYNOSA': (26.0312262, -98.3662435)
    , 'MONCLOVA': (26.907775, -101.4940069)
    , 'CIUDAD JUAREZ': (31.6538179, -106.5890206)
    , 'JANOS': (30.8898127, -108.208458)
    , 'CIUDAD OBREGON': (27.4827355, -110.0844111)
    , 'TORREON': (25.548597, -103.4719562)
    , 'OJINAGA': (29.5453292, -104.4305246)
    , 'NUEVO LAREDO': (27.4530856, -99.6881218)
    , 'AGUA PRIETA': (31.3115272, -109.5855873)
    , 'GUAYMAS': (27.9272572, -110.9779564)
    , 'PIEDRAS NEGRAS': (28.6910517, -100.5801829)
    , 'SANTA ANA': (30.5345457, -111.1580567)
    , 'HERMOSILLO': (29.082137, -111.059027)
    , 'MEXICALI': (32.6137391, -115.5203312)
    , 'TIJUANA': (32.4966818, -117.087892)
    , 'SAN FELIPE': (31.009535, -114.8727296)
    , 'ENSENADA': (31.8423096, -116.6799816)
    , 'SAN QUINTIN': (30.5711324, -115.9588544)
    , 'SANTA ROSALIA': (27.3408761, -112.2825762)
    , 'SANTO DOMINGO': (25.3487297, -111.9975909)
    , 'LA PAZ': (24.1164209, -110.3727673)
    , 'CABO SAN LUCAS': (22.8962253, -109.9505077)
}


def Haversine_heuristic(goal):
    # Estandarizamos el nombre de la ciudad objetivo para poder realizar la llamada de la función: 'haversine'
    goal_city = goal.upper()

    # diccionario que contendra los valores de la heuristica de distancia de haversine para
    # la ciudad de destino ingresada
    haversine_heuristic = {}

    # itera a traves de todas las ciudades disponibles en el grafo
    for city_origin in cities_coordinates:
        # obtiene la distancia de haversine de las dos ciudades correspondientes
        haversine_distance = haversine(city_origin, goal_city)
        # agrega al diccionario de heuristica la ciudad de origen y su valor de distancia de haversine
        haversine_heuristic[city_origin] = round(haversine_distance)

    # regresa el diccionario con los valores de la heuristica para la ciudad objetivo correspondiente

    print(haversine_heuristic)


def haversine(origin, goal):
    lat1 = cities_coordinates[origin][0]
    lon1 = cities_coordinates[origin][1]
    lat2 = cities_coordinates[goal][0]
    lon2 = cities_coordinates[goal][1]

    R = 6372.8  # this is the Earth radius in kilometers

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c

treeucp=[['CANCUN', [('VALLADOLID', 90), ('FELIPE CARRILLO PUERTO', 100)]], ['VALLADOLID', [('FELIPE CARRILLO PUERTO', 90)]], ['FELIPE CARRILLO PUERTO', [('CAMPECHE', 60)]], ['CAMPECHE', [('MERIDA', 90), ('CIUDAD DEL CARMEN', 90), ('CHETUMAL', 100)]], ['CIUDAD DEL CARMEN', [('VILLAHERMOSA', 90), ('TUXTLA', 90)]], ['CHETUMAL', [('FRANCISCO ESCARCEGA', 90)]], ['VILLAHERMOSA', [('ACAYUCAN', 90)]], ['TUXTLA', [('ACAYUCAN', 90)]], ['ACAYUCAN', [('TEHUANTEPEC', 80), ('ALVARADO', 110)]], ['ALVARADO', [('OAXACA', 100)]], ['OAXACA', [('PUERTO ANGEL', 90), ('IZUCAR DE MATAMOROS', 90), ('TEHUACAN', 80)]], ['PUERTO ANGEL', [('PINOTEPA NACIONAL', 100)]], ['IZUCAR DE MATAMOROS', [('CUERNAVACA', 100), ('PUEBLA', 90)]], ['PINOTEPA NACIONAL', [('ACAPULCO', 100)]], ['CUERNAVACA', [('CIUDAD DE MEXICO', 100), ('IGUALA', 100), ('CIUDAD ALTAMIRANO', 100)]], ['PUEBLA', [('CIUDAD DE MEXICO', 90), ('CORDOBA', 80)]], ['ACAPULCO', [('CHILPANCINGO', 140)]], ['CIUDAD DE MEXICO', [('TLAXCALA', 100), ('PACHUCA DE SOTO', 100), ('QUERETARO', 90), ('TOLUCA DE LERDO', 110)]], ['CIUDAD ALTAMIRANO', [('ZIHUATANEJO', 90)]], ['CORDOBA', [('VERACRUZ', 90)]], ['CHILPANCINGO', [('IGUALA', 90)]], ['PACHUCA DE SOTO', [('TUXPAN DE RODRIGUEZ CANO', 110)]], ['QUERETARO', [('ATLACOMULCO', 90), ('SALAMANCA', 90), ('SAN LUIS POTOSI', 90)]], ['TOLUCA DE LERDO', [('CIUDAD ALTAMIRANO', 100)]], ['ZIHUATANEJO', [('PLAYA AZUL', 90)]], ['TUXPAN DE RODRIGUEZ CANO', [('TAMPICO', 80)]], ['SALAMANCA', [('GUANAJUATO', 90), ('MORELIA', 90), ('GUADALAJARA', 90)]], ['SAN LUIS POTOSI', [('AGUASCALIENTES', 100), ('ZACATECAS', 90), ('DURANGO', 70)]], ['PLAYA AZUL', [('COLIMA', 100), ('MANZANILLO', 100)]], ['TAMPICO', [('CIUDAD VICTORIA', 80)]], ['GUANAJUATO', [('AGUASCALIENTES', 80)]], ['GUADALAJARA', [('TEPIC', 110)]], ['AGUASCALIENTES', [('GUADALAJARA', 70)]], ['DURANGO', [('HIDALGO DEL PARRAL', 90), ('MAZATLAN', 90)]], ['COLIMA', [('GUADALAJARA', 50), ('MANZANILLO', 50)]], ['MANZANILLO', [('GUADALAJARA', 80)]], ['CIUDAD VICTORIA', [('DURANGO', 80), ('SOTO LA MARINA', 80), ('MATAMOROS', 80), ('MONTERREY', 80)]], ['TEPIC', [('MAZATLAN', 110)]], ['HIDALGO DEL PARRAL', [('CHIHUAHUA', 130), ('TOPOLOBAMPO', 110), ('CULIACAN', 80)]], ['MAZATLAN', [('CULIACAN', 90)]], ['MATAMOROS', [('REYNOSA', 90)]], ['MONTERREY', [('MONCLOVA', 70)]], ['CHIHUAHUA', [('CIUDAD JUAREZ', 90), ('JANOS', 90)]], ['TOPOLOBAMPO', [('CIUDAD OBREGON', 90)]], ['CULIACAN', [('TOPOLOBAMPO', 110)]], ['REYNOSA', [('NUEVO LAREDO', 90)]], ['MONCLOVA', [('TORREON', 110), ('OJINAGA', 110)]], ['JANOS', [('AGUA PRIETA', 110)]], ['CIUDAD OBREGON', [('GUAYMAS', 80)]], ['TORREON', [('DURANGO', 110)]], ['OJINAGA', [('CHIHUAHUA', 90)]], ['NUEVO LAREDO', [('MONTERREY', 110), ('PIEDRAS NEGRAS', 100)]], ['AGUA PRIETA', [('SANTA ANA', 110)]], ['GUAYMAS', [('HERMOSILLO', 80)]], ['PIEDRAS NEGRAS', [('MONCLOVA', 100)]], ['SANTA ANA', [('MEXICALLI', 150)]], ['HERMOSILLO', [('SANTA ANA', 60)]], ['MEXICALLI', [('TIJUANA', 110), ('SAN FELIPE', 70)]], ['TIJUANA', [('ENSENADA', 50)]], ['SAN FELIPE', [('ENSENADA', 50)]], ['ENSENADA', [('SAN QUINTIN', 60)]], ['SAN QUINTIN', [('SANTA ROSALIA', 60)]], ['SANTA ROSALIA', [('SANTO DOMINGO', 60)]], ['SANTO DOMINGO', [('LA PAZ', 70)]], ['LA PAZ', [('CABO SAN LUCAS', 70)]]]


def primero_voraz(tree,start,goal,heuristica):
  path = [start]

  if start == goal:
    return path

  while True:
    nodo_actual = path[-1]

    hijos = [node_weights_list[1] for node_weights_list in tree[1] if node_weights_list[0] == nodo_actual]

    #print(hijos)

    hijos_con_h = []

    for hijo in hijos[0]: ##aqui marca error
          #print(hijo)
          valor_h = heuristica[hijo[0]]
          hijos_con_h.append((hijo[0],valor_h))

  #  print(hijos_con_h)
        #[('Timisoara', 329), ('Sibiu', 253), ('Zerind', 374)]

    valor_minimo = min(hijos_con_h)
    #print(valor_minimo)

    path.append(valor_minimo[0])

   # print(path)

    if path[-1] == goal:
         return path

def A_search(tree,start,goal,heuristica):
  path = [start]

  if start == goal:
    return path

  while True:
    nodo_actual = path[-1]

    hijos = [node_weights_list[1] for node_weights_list in tree[1] if node_weights_list[0] == nodo_actual]

    #print(hijos)

    hijos_funcion=[]

    for hijo in hijos[0]: ##aqui marca error
          #print(hijo)
          valor_h = heuristica[hijo[0]]
          valor_f=hijo[1]+valor_h
          hijos_funcion.append((hijo[0],valor_f))
                       
    valor_minimo = min(hijos_funcion)
    #print(valor_minimo)
    path.append(valor_minimo[0])
    #print(path)

    if path[-1] == goal:
         return path 
    
def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup

def beam_search(tree, start, goal, beam_width, heuristica):
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
            h_last_nodes.append((node, heuristica[node])) ##aqui marcca error
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
            value_h = heuristica[neighbor[0]]
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
            aux_with_h.append((node, heuristica[node]))

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

        return branches
    

start="cancun"
goal="cabo san lucas"

Goal_hsh=Haversine_heuristic(goal)
#A_search(treeucp,start,goal,Goal_hsh)
#primero_voraz(treeucp,start,goal,Goal_hsh)

beam_search(treeucp, start, goal, 2, Goal_hsh)




