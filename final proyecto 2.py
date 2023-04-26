"""
PROYECTO SEGUNDO PARCIAL: ALGORITMOS DE BÚSQUEDA INFORMADOS
UNIVERSIDAD PANAMERICANA
    MATERIA: INTELIGENCIA ARTIFICIAL

INTREGRANTES:
    Emiliano Bojorquez Robles
    Fernanda Arizbé Torres Martínez
    Jimena Cuevas Sánchez

Fecha de entrega:26 de abril 2023

En este código, se realizará la implementación de los algoritmos de búsqueda
vistos en clase haciendo uso del grafo de las ciudades de México y la heurística
Haversine. 

Ejecución del programa
    Opción 1) En una terminal que sobre el directorio donde radica este archivo escribir:
                    python get_euclidean_distance.py
    Opción 2) Abrir el archivo con un editor de codigo y presionar el boton ejecutar
"""
####################################################################################################################################
#Dependencias: 
import math
from math import radians, cos, sin, asin, sqrt
import time 

#############################################################################################################################################
##### Variables Globales #####

# Diccionario con el nombre de las ciudades contenidas en el grafo y sus correspondientes coordenadas
# geograficas en formato de latitud y longitud
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

#Arbol con las ciudades de México, sus hijos, conexiones y pesos. 
treecp=[['CANCUN', [('VALLADOLID', 90), ('FELIPE CARRILLO PUERTO', 100)]], ['VALLADOLID', [('FELIPE CARRILLO PUERTO', 90)]], ['FELIPE CARRILLO PUERTO', [('CAMPECHE', 60)]], ['CAMPECHE', [('MERIDA', 90), ('CIUDAD DEL CARMEN', 90), ('CHETUMAL', 100)]], ['CIUDAD DEL CARMEN', [('VILLAHERMOSA', 90), ('TUXTLA', 90)]], ['CHETUMAL', [('FRANCISCO ESCARCEGA', 90)]], ['VILLAHERMOSA', [('ACAYUCAN', 90)]], ['TUXTLA', [('ACAYUCAN', 90)]], ['ACAYUCAN', [('TEHUANTEPEC', 80), ('ALVARADO', 110)]], ['ALVARADO', [('OAXACA', 100)]], ['OAXACA', [('PUERTO ANGEL', 90), ('IZUCAR DE MATAMOROS', 90), ('TEHUACAN', 80)]], ['PUERTO ANGEL', [('PINOTEPA NACIONAL', 100)]], ['IZUCAR DE MATAMOROS', [('CUERNAVACA', 100), ('PUEBLA', 90)]], ['PINOTEPA NACIONAL', [('ACAPULCO', 100)]], ['CUERNAVACA', [('CIUDAD DE MEXICO', 100), ('IGUALA', 100), ('CIUDAD ALTAMIRANO', 100)]], ['PUEBLA', [('CIUDAD DE MEXICO', 90), ('CORDOBA', 80)]], ['ACAPULCO', [('CHILPANCINGO', 140)]], ['CIUDAD DE MEXICO', [('TLAXCALA', 100), ('PACHUCA DE SOTO', 100), ('QUERETARO', 90), ('TOLUCA DE LERDO', 110)]], ['CIUDAD ALTAMIRANO', [('ZIHUATANEJO', 90)]], ['CORDOBA', [('VERACRUZ', 90)]], ['IGUALA',[('CIUDAD ALTAMIRANO',110)]],['CHILPANCINGO', [('IGUALA', 90)]], ['PACHUCA DE SOTO', [('TUXPAN DE RODRIGUEZ CANO', 110)]], ['QUERETARO', [('ATLACOMULCO', 90), ('SALAMANCA', 90), ('SAN LUIS POTOSI', 90)]], ['TOLUCA DE LERDO', [('CIUDAD ALTAMIRANO', 100)]], ['ZIHUATANEJO', [('PLAYA AZUL', 90)]], ['TUXPAN DE RODRIGUEZ CANO', [('TAMPICO', 80)]], ['SALAMANCA', [('GUANAJUATO', 90), ('MORELIA', 90), ('GUADALAJARA', 90)]], ['SAN LUIS POTOSI', [('AGUASCALIENTES', 100), ('ZACATECAS', 90), ('DURANGO', 70)]], ['PLAYA AZUL', [('COLIMA', 100), ('MANZANILLO', 100)]], ['TAMPICO', [('CIUDAD VICTORIA', 80)]], ['GUANAJUATO', [('AGUASCALIENTES', 80)]], ['GUADALAJARA', [('TEPIC', 110)]], ['AGUASCALIENTES', [('GUADALAJARA', 70)]], ['DURANGO', [('HIDALGO DEL PARRAL', 90), ('MAZATLAN', 90)]], ['COLIMA', [('GUADALAJARA', 50), ('MANZANILLO', 50)]], ['MANZANILLO', [('GUADALAJARA', 80)]], ['CIUDAD VICTORIA', [('DURANGO', 80), ('SOTO LA MARINA', 80), ('MATAMOROS', 80), ('MONTERREY', 80)]], ['TEPIC', [('MAZATLAN', 110)]], ['HIDALGO DEL PARRAL', [('CHIHUAHUA', 130), ('TOPOLOBAMPO', 110), ('CULIACAN', 80)]], ['MAZATLAN', [('CULIACAN', 90)]], ['MATAMOROS', [('REYNOSA', 90)]], ['MONTERREY', [('MONCLOVA', 70)]], ['CHIHUAHUA', [('CIUDAD JUAREZ', 90), ('JANOS', 90)]], ['TOPOLOBAMPO', [('CIUDAD OBREGON', 90)]], ['CULIACAN', [('TOPOLOBAMPO', 110)]], ['REYNOSA', [('NUEVO LAREDO', 90)]], ['MONCLOVA', [('TORREON', 110), ('OJINAGA', 110)]], ['JANOS', [('AGUA PRIETA', 110)]], ['CIUDAD OBREGON', [('GUAYMAS', 80)]], ['TORREON', [('DURANGO', 110)]], ['OJINAGA', [('CHIHUAHUA', 90)]], ['NUEVO LAREDO', [('MONTERREY', 110), ('PIEDRAS NEGRAS', 100)]], ['AGUA PRIETA', [('SANTA ANA', 110)]], ['GUAYMAS', [('HERMOSILLO', 80)]], ['PIEDRAS NEGRAS', [('MONCLOVA', 100)]], ['SANTA ANA', [('MEXICALI', 150)]], ['HERMOSILLO', [('SANTA ANA', 60)]], ['MEXICALI', [('TIJUANA', 110), ('SAN FELIPE', 70)]], ['TIJUANA', [('ENSENADA', 50)]], ['SAN FELIPE', [('ENSENADA', 50)]], ['ENSENADA', [('SAN QUINTIN', 60)]], ['SAN QUINTIN', [('SANTA ROSALIA', 60)]], ['SANTA ROSALIA', [('SANTO DOMINGO', 60)]], ['SANTO DOMINGO', [('LA PAZ', 70)]], ['LA PAZ', [('CABO SAN LUCAS', 70)]]]

##### Funciones o Clases de Apoyo #####

# Calcula la distancia euclideana entre dos ciudades por medio de las coordenas geograficas

# Entrada:
    # origin = tupla que contiene la latitud y longitud de la ciudad de origen
    # goal = tupla que contiene la latitud y longitud de la ciudad destino

# Salida:
    #regresa el valor numerico de la distancia euclideana redondeado
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

# Función: Heurística de Haversine: Calcula la heuristica para una ciudad objetivo

# Entrada:
    # goal = nombre de la ciudad objetivo

# Salida:
    # Regresa un diccionario con los valores numericos de la heuristica para la ciudad objetivo
    # introducida por el usuario
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

    return(haversine_heuristic)

#Función: Sort Tuple, ordena una tupla de tuplas en base al segundo elemento de cada tupla, de manera ascendente.

#Entrada:
    #tup: tupla que se desea ordenar

#Salida:
    #tup: tupla ordenada
def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup
#################################################################################################################
#Responsable: Fer
#Función: "Primero Voraz", calcula el camino entre dos ciudades con la heuristica de Haversine yendo siempre por el valor
#más bajo de la misma

#Entradas: 
    #-tree: arbol
    #-start: ciudad de inicio
    #-goal: ciudad objetivo
    #-heuristica: diccionario con la heuristica calculada para nuestra ciudad obejtivo
    #-bandera: Indicador que nos informa si el usuario pidió mostrar el paso a paso del algoritmo. Si es así, imprime a
    #lo largo del algoritmo el procedimiento hecho

#Salida: 
    # "path" nos devuelve una tupla cuyo primer elemento es una lista que contiene el camino desde nuestra ciudad de 
    # inicio a nuestra ciudad objetivo y el segundo el tiempo de ejecución del algoritmo
def primero_voraz(tree,start,goal,heuristica,bandera):
  start_time = time.time()
  path = [start]

    #Si nuestra ciudad de inicio es igual a nuestro destino, nos devuelve el camino con la ciudad de inicio
  if start == goal:
    end_time = time.time()
    tiempo=end_time-start_time
    return path, tiempo

  while True:
    #nuestro nodo actual siempre será el último de nuestro camino
    nodo_actual = path[-1]
    if bandera==1:
        print("el nodo actual es ", nodo_actual)
   
    #Hacemos una lista con los hijos de nuestro nodo actual para poder explorarlos
    hijos = [node_weights_list[1] for node_weights_list in tree if node_weights_list[0] == nodo_actual]
    
    if bandera==1:
        print("la lista de hijos es ", hijos)

    hijos_con_h = []
    
    #cambiamos los pesos de nuestro hijos por los valores de nuestra heurística
    for hijos0 in hijos:
          for hijo in hijos0:
                if bandera==1:
                    print(hijo)
                valor_h = heuristica[hijo[0]]
                hijos_con_h.append((hijo[0],valor_h))

    if bandera==1:
        print("los hijos con heurística son ", hijos_con_h)
        
    #ordena los hijos con los nuevos valores de la heurística y elije el de valor mínimo
    valor_minimo=hijos_con_h[0]
    for hijo in hijos_con_h:
       if hijo[1]<valor_minimo[1]:
          valor_minimo=hijo

    if bandera==1:
        print("el valor minimo de los hijos con h es ", valor_minimo)

    #agrega a nuestro camino el hijo de valor minimo pues es el que está más cerca de nuestro destino
    path.append(valor_minimo[0])

    if bandera==1:
        print("El camino hasta ahora es ", path)

    print("\n")

    if path[-1] == goal:
        end_time = time.time()
        tiempo=end_time-start_time
        return path, tiempo
    
    
    
###################################################################################################################################
#Responsable: Fer
#Función: "A* search", calcula el camino entre dos ciudades con la heuristica de Haversine yendo siempre por el valor
#más bajo de los pesos entre las ciudades más el valor de la heuristica para la ciudad objetivo

#Entradas: 
    #-tree: arbol
    #-start: ciudad de inicio
    #-goal: ciudad objetivo
    #-heuristica: diccionario con la heuristica calculada para nuestra ciudad obejtivo
    #-bandera: Indicador que nos informa si el usuario pidió mostrar el paso a paso del algoritmo. Si es así, imprime a
    #lo largo del algoritmo el procedimiento hecho

#Salida: 
    # "path" nos devuelve una tupla cuyo primer elemento es una lista que contiene el camino desde nuestra ciudad de 
    # inicio a nuestra ciudad objetivo y el segundo el tiempo de ejecución del algoritmo
def A_search(tree,start,goal,heuristica, bandera):
  start_time = time.time()
  path = [start]
    #Si nuestra ciudad de inicio es igual a nuestro destino, nos devuelve el camino con la ciudad de inicio
  if start == goal:
    end_time = time.time()
    tiempo=end_time-start_time
    return path

  while True:
    #nuestro nodo actual siempre será el último de nuestro camino
    nodo_actual = path[-1]

    if bandera==1:
        print("el nodo actual es ", nodo_actual)

    #Hacemos una lista con los hijos de nuestro nodo actual para poder explorarlos
    hijos = [node_weights_list[1] for node_weights_list in tree if node_weights_list[0] == nodo_actual]
    

    if bandera==1:
        print("la lista de hijos es ", hijos)

    hijos_con_h = []
    
    #cambiamos los pesos de nuestro hijos por los valores originales más los 
    # de nuestra heurística 
    for hijos0 in hijos:
          for hijo in hijos0:
            if bandera==1:
                    print(hijo)
            valor_h = heuristica[hijo[0]]
            valor_f=hijo[1]+valor_h
            hijos_con_h.append((hijo[0],valor_f))

    if bandera==1:
        print("los hijos con heurística son ", hijos_con_h)
        
    #ordena los hijos con los nuevos valores de la heurística y elije el de valor mínimo
    valor_minimo=hijos_con_h[0]
    for hijo in hijos_con_h:
       if hijo[1]<=valor_minimo[1]:
          valor_minimo=hijo

    if bandera==1:
        print("el valor minimo de los hijos con heurística es ", valor_minimo)

    #agrega a nuestro camino el hijo de valor minimo pues es el que está más cerca de nuestro destino
    path.append(valor_minimo[0])

    if bandera==1:
        print("el camino hasta ahora es ", path)
    print("\n")

    if path[-1] == goal:
        end_time = time.time()
        tiempo=end_time-start_time
        return path, tiempo

#############################################################################################################################3
#Responsable: Fer
#Función: "Weighted A* search", calcula el camino entre dos ciudades con la heuristica de Haversine yendo siempre por el valor
#más bajo de los pesos entre las ciudades más el valor de la heuristica para la ciudad objetivo considerando nuestro 
#índice de desvío 

#Entradas: 
    #-tree: arbol
    #-start: ciudad de inicio
    #-goal: ciudad objetivo
    #-heuristica: diccionario con la heuristica calculada para nuestra ciudad obejtivo
    #-bandera: Indicador que nos informa si el usuario pidió mostrar el paso a paso del algoritmo. Si es así, imprime a
    #lo largo del algoritmo el procedimiento hecho

#Salida: 
    # "path" nos devuelve una tupla cuyo primer elemento es una lista que contiene el camino desde nuestra ciudad de 
    # inicio a nuestra ciudad objetivo y el segundo el tiempo de ejecución del algoritmo
def weighted_A_search(tree,start,goal,heuristica,bandera):
  start_time = time.time()
  path = [start]

  #Si nuestra ciudad de inicio es igual a nuestro destino, nos devuelve el camino con la ciudad de inicio
  if start == goal:
    end_time = time.time()
    tiempo=end_time-start_time
    return path

  while True:
    #nuestro nodo actual siempre será el último de nuestro camino
    nodo_actual = path[-1]
    if bandera==1:
        print("el nodo actual es ", nodo_actual)

    #Hacemos una lista con los hijos de nuestro nodo actual para poder explorarlos
    hijos = [node_weights_list[1] for node_weights_list in tree if node_weights_list[0] == nodo_actual]
    

    if bandera==1:
        print("la lista de hijos es ", hijos)

    hijos_con_h = []
    
    #cambiamos los pesos de nuestro hijos por los valores originales más los 
    # de nuestra heurística considerando el índice de desvío
    for hijos0 in hijos:
          for hijo in hijos0:
            if bandera==1:
                    print(hijo)
            valor_h = heuristica[hijo[0]]
            valor_f=hijo[1]+(1.3*valor_h)
            hijos_con_h.append((hijo[0],valor_f))

    if bandera==1:
        print("los hijos con heurística son ", hijos_con_h)

    #ordena los hijos con los nuevos valores de la heurística y elije el de valor mínimo
    valor_minimo=hijos_con_h[0]
    for hijo in hijos_con_h:
       if hijo[1]<=valor_minimo[1]:
          valor_minimo=hijo

    if bandera==1:
        print("el valor minimo de los hijos con h es ", valor_minimo)

    #agrega a nuestro camino el hijo de valor minimo pues es el que está más cerca de nuestro destino    
    path.append(valor_minimo[0])

    if bandera==1:
        print("el camino hasta ahora es ", path)
    print("\n")

    if path[-1] == goal:
        end_time = time.time()
        tiempo=end_time-start_time
        return path, tiempo


#############################################################################################################
#Responsable: Emiliano
#Función: "Beam Search", funciona seleccionando hijos aleatorios de una lista de ciudades.El algoritmo se basa en la 
# utilización de un parámetro denominado "beam_width" para determinar el número de resultados que se 
# seleccionan en cada iteración.

#Entradas: 
    #-tree: arbol
    #-start: ciudad de inicio
    #-goal: ciudad objetivo
    #-heuristica: diccionario con la heuristica calculada para nuestra ciudad obejtivo
    #-beam_width:es la cantidad de hijos que expandirá en cada iteración
    #-bandera: Indicador que nos informa si el usuario pidió mostrar el paso a paso del algoritmo. Si es así, imprime a
    #lo largo del algoritmo el procedimiento hecho

#Salida: 
    # "path" nos devuelve una tupla cuyo primer elemento es una lista que contiene el camino desde nuestra ciudad de 
    # inicio a nuestra ciudad objetivo y el segundo el tiempo de ejecución del algoritmo

def beam_search(tree, start, goal, beam_width, heuristic,flag):
    start_time = time.time()
    global branch
    nodes_visited = []
    branches = [[start]]

    while branches:
        #  this piece of code ensures that we always take the lowest heuristic value node
        last_nodes = [path[-1] for path in
                      branches]  # we create a list with the last nodes of all of our possible paths
        if flag==1:
          print('\nThese are the last nodes from all possible paths:', last_nodes)
        h_last_nodes = []
        for node in last_nodes:
            h_last_nodes.append((node, heuristic[node]))

        if flag==1:
          print('\nThis is h_last_nodes list:', h_last_nodes)

        lowest_h_value = min(h_last_nodes)
        if flag==1:
          print('\nThis is the lowest value from h_las_nodes list:', lowest_h_value)
        key_node = lowest_h_value[0]

        for path in branches:
            if key_node == path[-1]:
                branch = path
                branches.remove(path)
                break

        if flag==1:
          print('----')
          print('\nBranches available: ', branches)
          print('\nbranch to explore: ', branch)
          print('\nnodes visited: ', nodes_visited)

        current_node = branch[-1]  # we take the last node of our possible path as our current node
       
        if flag==1:
          print('\ncurrent node ', current_node)

        # checks if the node where we are located is the stop
        if current_node == goal:
            end_time = time.time()
            tiempo=end_time-start_time
            return branch, tiempo

        if current_node not in nodes_visited:
            nodes_visited.append(current_node)

        if flag==1:
            print('\nThese are the nodes that have been visited:', nodes_visited)

        neighbors_with_h = []
        # we get the neighbors of every node as we did in greedy
        node_neighbors = [node_weights_list[1] for node_weights_list in tree if node_weights_list[0] == current_node]
        if flag==1:
          print(f"\nThese are the neighbors of node {current_node}: ", node_neighbors)

        for neighbor in node_neighbors[0]:  # itera en cada hijo
            value_h = heuristic[neighbor[0]]
            neighbors_with_h.append((neighbor[0], value_h))

        if flag==1:
          print(f"\nThis the the updated list (taking into account heuristic) of neighbors of node {current_node}: ",
              neighbors_with_h)

        sorted_neighbors = Sort_Tuple(neighbors_with_h)
        
        if flag==1:
          print(f"\nThis is the sorted list of neighbors of node {current_node}: {sorted_neighbors}")

        for neighbor in sorted_neighbors[0:beam_width]:  # *******
            if flag==1:
              print('\nCurrently exploring neighbor:', neighbor[0])
            if neighbor[0] == goal:
                branch.append(neighbor[0])
                end_time = time.time()
                tiempo=end_time-start_time
                return branch, tiempo

            if neighbor[0] not in nodes_visited:
                updated_branch = branch.copy()
                if flag==1:
                  print('\nThis is the updated branch: ', updated_branch)
                updated_branch.append(neighbor[0])
                if flag==1:
                  print('\nThis is the updated branch, having appended the neighbor: ', updated_branch)
                branches.append(updated_branch)
                if flag==1:
                  print('\nThis is branches: ', branches)

#####################################################################################################################################
#Responsable: Emiliano
#Función: "Steepest Ascent Hill", es una técnica de búsqueda local que mueve un punto en la dirección del valor 
# más alto de la heuristica en cada iteración, deteniéndose cuando no se puede encontrar una mejor solución en 
# la vecindad actual. Sin embargo, puede quedar atrapado en óptimos locales y no encontrar el óptimo global.

#Entradas: 
    #-tree: arbol
    #-start: ciudad de inicio
    #-goal: ciudad objetivo
    #-heuristic: diccionario con la heuristica calculada para nuestra ciudad obejtivo
    #-bandera: Indicador que nos informa si el usuario pidió mostrar el paso a paso del algoritmo. Si es así, imprime a
    #lo largo del algoritmo el procedimiento hecho

#Salida: 
    # "path" nos devuelve una tupla cuyo primer elemento es una lista que contiene el camino desde nuestra ciudad de 
    # inicio a nuestra ciudad objetivo (si es que lo encontró) y el segundo el tiempo de ejecución del algoritmo

def Steepest_Ascent_Hill_Climber(tree, start, goal, heuristic, flag):
    banned_nodes = ['MERIDA', 'FRANCISCO ESCARCEGA', 'TEHUANTEPEC', 'TEHUACAN', 'IGUALA', 'TLAXCALA', 'VERACRUZ',
                'ATLACOMULCO', 'MORELIA', 'ZACATECAS', 'SOTO LA MARINA', 'CIUDAD JUAREZ', 'SANTA ANA', 'CABO SAN LUCAS']
    start_time = time.time()
    nodes_visited = []
    branches = [[start]]

    while branches:
        if flag==1:
          print('----')
          print('\nBranches available: ', branches)
        branch = branches.pop()
        if flag==1:
          print('\nbranch to explore: ', branch)
          print('\nnodes visited: ', nodes_visited)

        current_node = branch[-1]  # we take the last node of our possible path as our current node
        if flag==1:
          print('\ncurrent node ', current_node)

        # checks if the node where we are located is the stop
        if current_node == goal:
            end_time = time.time()
            tiempo=end_time-start_time
            return branch, tiempo

        if current_node not in nodes_visited:
            nodes_visited.append(current_node)
        
        if flag==1:
          print('\nThese are the nodes that have been visited:', nodes_visited)

        current_h = heuristic[current_node]

        for node_weights_list in tree:
            if node_weights_list[0] == current_node:
                if flag==1:
                  print(f'\nThese are the neighbors of node {current_node}: {node_weights_list[1]}')
                while len(node_weights_list[1]) >= 1:  # we keep extracting neighbours as long as there's at least one
                    # neighbor
                    if flag==1:
                      print(f'\nThis is the list of neighbors of node {current_node}:', node_weights_list[1])
                    neighbor = node_weights_list[1].pop()  # we opt to select the neighbor at the end
                    if neighbor[0] in banned_nodes: # if our initial choice of neighbor happens to be in the list of
                        # banned cities, we pick another one (if available)
                        neighbor = node_weights_list[1].pop()
                    
                    if flag==1:
                      print(f'\nExploring neighbor: {neighbor}')
                    neighbor_h = heuristic[neighbor[0]]  # we get the neighbor's heuristic value
                    if flag==1:
                      print(
                        f'\nThis is heuristic value of node {neighbor[0]}: {neighbor_h} vs the current heuristic: {current_h}')
                    if neighbor_h < current_h:
                        branch.append(neighbor[0])
                        if branch[-1] == goal:
                            end_time = time.time()
                            tiempo=end_time-start_time
                            return branch, tiempo
                        else:
                            updated_branch = branch.copy()
                            if flag==1:
                              print('\nThis is the updated branch, since a new maximum heuristic value has been found:',
                                  updated_branch)
                            branches.append(updated_branch)
                            if flag==1:
                              print('\nThis is branches: ', branches)
                            break



########################################################################################################################################
#######FUNCIONES PRINCIPALES##########
#Esta función es la encargada de pedirle al usuario la ciudad de incio y la ciudad objetivo. También realiza una 
#validación para que las ciudades estén dentro de las ciudades permitidas.

#Responsable:Fer
#Entrada:
    #No necesita parametros de entrada 

#Salida:
    #No regresa nada 

def main():
    ciudades = ['CANCUN','VALLADOLID','FELIPE CARRILLO PUERTO','CAMPECHE','MERIDA','CIUDAD DEL CARMEN','CHETUMAL','VILLAHERMOSA','TUXTLA','FRANCISCO ESCARCEGA','ACAYUCAN', 'TEHUANTEPEC','ALVARADO','OAXACA','PUERTO ANGEL','IZUCAR DE MATAMOROS','TEHUACAN','PINOTEPA NACIONAL','CUERNAVACA','PUEBLA','ACAPULCO','CIUDAD DE MEXICO','IGUALA','CIUDAD ALTAMIRANO','CORDOBA','CHILPANCINGO','TLAXCALA','PACHUCA DE SOTO','QUERETARO','TOLUCA DE LERDO','ZIHUATANEJO','VERACRUZ','TUXPAN DE RODRIGUEZ CANO','ATLACOMULCO','SALAMANCA','SAN LUIS POTOSI','PLAYA AZUL','TAMPICO','GUANAJUATO','MORELIA','GUADALAJARA','AGUASCALIENTES','ZACATECAS','DURANGO','COLIMA','MANZANILLO','CIUDAD VICTORIA','TEPIC','HIDALGO DEL PARRAL','MAZATLAN','SOTO LA MARINA','MATAMOROS','MONTERREY','CHIHUAHUA','TOPOLOBAMPO','CULIACAN','REYNOSA','MONCLOVA','CIUDAD JUAREZ','JANOS','CIUDAD OBREGON','TORREON','OJINAGA','NUEVO LAREDO','AGUA PRIETA','GUAYMAS','PIEDRAS NEGRAS','SANTA ANA','HERMOSILLO','MEXICALI','TIJUANA','SAN FELIPE','ENSENADA','SAN QUINTIN','SANTA ROSALIA','SANTO DOMINGO','LA PAZ','CABO SAN LUCAS']
    start='p'
    goal='c'
    bandera=-1
    
    while start not in ciudades:
        start=input("Ingrese la ciudad desde la que desea iniciar su búsqueda: ").upper()
    
    while goal not in ciudades:
        goal=input("Ingrese la ciudad a la que desea llegar: ").upper()

    while bandera!=1 and bandera!=0:
        bandera=int(input("Si quiere la información paso a paso presione 1, si no, presione 0: "))

    menu(start,goal,bandera)
 
#Responsable:Fer
def menu(start,goal,bandera):
    Goal_hsh=Haversine_heuristic(goal)
    opc=-1

    while True:
        print('\n\t\tProyecto Segundo parcial')
        print('\t1. Greedy Best-First:')
        print('\t2. A* Search:')
        print('\t3. Weighted A* Search:')
        print('\t4. Beam Search:')
        print('\t5. Steepest hill cllimbing: ')
        print('\t6. Stochastic hill cllimbing: ')
        print('\t7. Simulated annealing: ')
        print('\t8. Salir')
        opc = int(input('\n\tDe la opción de la búsqueda que desea realizar: '))
        
                            
        if opc==1:
            print("\nGreedy Best-First: ")
            result1 = primero_voraz(treecp, start, goal,Goal_hsh,bandera)
            print('\nThe path from {} to {} is {}'.format(start, goal, result1[0]))
            print('\nThe Greedy Best-First Search algorithm exuction time is {}\n'.format(result1[1]))

        if opc==2:
            print("\nA* Search:: ")
            result2 = A_search(treecp, start, goal,Goal_hsh,bandera)
            print('\nThe path from {} to {} is {}\n'.format(start, goal, result2[0]))
            print('\nThe A* Search algorithm exuction time is {}\n'.format(result2[1]))
                
        if opc==3:
            print("\nWeighted A* Search: ")
            result3 = weighted_A_search(treecp, start, goal,Goal_hsh,bandera)
            print('\nThe path from {} to {} is {}\n'.format(start, goal, result3[0]))
            print('\nThe Weighted A* Search algorithm exuction time is {}\n'.format(result3[1]))

        if opc==4:
            print("\nBeam Search:: ")

            while beam_width<=0:
                 beam_width=int(input("Ingrese la amplitud de rayo que desee usar: "))

            result4 = beam_search(treecp, start, goal, beam_width,Goal_hsh,bandera)
            print('\nThe path from {} to {} is {}\n'.format(start, goal, result4[0]))
            print('\nThe Beam Search algorithm exuction time is {}\n'.format(result4[1]))


        if opc==5:
            print("\nSteepest  Hill Climbing: ")
            result5 = Steepest_Ascent_Hill_Climber(treecp, start, goal, Goal_hsh, bandera)
            print('\nThe path from {} to {} is {}\n'.format(start, goal, result5[0]))
            print('\nThe Beam Search algorithm exuction time is {}\n'.format(result5[1]))


        """""
        if opc==6:
            print("\nSteepest Hill Climbing: ")
            route = bidirectional_search(start, goal)
            print(route)

        if opc==7:
            print("\nSimulated annealing: ")
            route = bidirectional_search(start, goal)
            print(route)
        """""
                  
        if opc == 8:
            print('\nMuchas gracias, hasta luego.')
            break
        else:
            print('Favor de seleccionar una opción válida.')
    

main()   

