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
    Opción 1) Abrir el archivo con un editor de codigo y presionar el boton ejecutar
"""
####################################################################################################################################
#Dependencias: 
import math
from math import radians, cos, sin, asin, sqrt
import time 
import networkx # Hay que revisar que esté instalado. En la terminal poner 'pip list'. Para instalarlo: 'pip install networkx'.
import random

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

#############################################################################################################################
##### Funciones o Clases de Apoyo #####

# Calcula la distancia de haversine entre dos ciudades por medio de las coordenas geograficas

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
###########################################################################################3
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
######################################################################################
#Función: Sort Tuple, ordena una lista de tuplas en base al segundo elemento de cada tupla, de manera ascendente.

#Entrada:
    #tup: lisata de tuplas que se desea ordenar

#Salida:
    #tup: lista ordenada
def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1])
    return tup

###################################################################################
#Función: Approved_n, La función filtra los vecinos que no están presentes en el árbol y devuelve una lista 
# con los vecinos aprobados.

#Entrada:
    #neigh_list: una lista de vecinos
    #tree: arbol

#Salida:
    #tup: tupla ordenada
def Approved_n(neigh_list, tree):
    final_n = []

    for neighbor in neigh_list:
        current_node = neighbor[0]
        node_neighbors = [node_weights_list[1] for node_weights_list in tree if node_weights_list[0] == current_node]
        if len(node_neighbors) != 0:
            final_n.append(neighbor)

    return final_n


#################################################################################################################
########################################################################################################################################
#######FUNCIONES PRINCIPALES##########
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

        for neighbor in node_neighbors[0]:  # se itera en cada hijo para obtener una nueva lista de tuplas, con los correspondientes valores heurísticos de cada vecino y su nombre
            value_h = heuristic[neighbor[0]]
            neighbors_with_h.append((neighbor[0], value_h))

        if flag==1:
          print(f"\nThis the the updated list (taking into account heuristic) of neighbors of node {current_node}: ",
              neighbors_with_h)

        sorted_neighbors = Sort_Tuple(neighbors_with_h) # llamamos a la función 'Sort_tuple' para ordenar la lista de vecinos ascendemente según el segundo valor de las tuplas
        
        if flag==1:
          print(f"\nThis is the sorted list of neighbors of node {current_node}: {sorted_neighbors}")

        for neighbor in sorted_neighbors[0:beam_width]:  # Restringimos nuestra lista de vecinos al ancho del rayo
            if flag==1:
              print('\nCurrently exploring neighbor:', neighbor[0])
            if neighbor[0] == goal:
                branch.append(neighbor[0])
                end_time = time.time()
                tiempo=end_time-start_time
                return branch, tiempo

            if neighbor[0] not in nodes_visited: #agregamos cada vecino al final de nuestras ramas o posibles caminos y las agregamos a la lista de todos los posibles caminos ('branches')
                updated_branch = branch.copy()
                if flag==1:
                  print('\nThis is the updated branch: ', updated_branch)
                updated_branch.append(neighbor[0])
                if flag==1:
                  print('\nThis is the updated branch, having appended the neighbor: ', updated_branch)
                branches.append(updated_branch)
                if flag==1:
                  print('\nThis is branches: ', branches)
                
        # *********************************************************************************************************
        if flag==1:
          print("\nThis is 'branches' before restricting it to beam_width :", branches)
        aux = [possible_path[-1] for possible_path in
               branches]  # we create a list with the last nodes of all of our possible paths
        if flag==1:
          print('\nThese are the last nodes from all possible paths:', aux)

        aux_with_h = []
        for node in aux:
            aux_with_h.append((node, heuristic[node]))

        if flag==1:
          print('\nThis is aux_with_h list:', aux_with_h)
        sorted_aux_list = Sort_Tuple(aux_with_h)
        if flag==1:
          print(f"\nFirst we sort our list: {sorted_aux_list}")

        cool_list = sorted_aux_list[0:beam_width]  # we restrict the number of paths to be explored
        aux_2 = []
        for tup in cool_list:
            aux_2.append(tup[0])
        if flag==1:
          print(f"\nThis is the nodes we're interested in, since they've got the lowest heuristic values: {aux_2}")
        for path in branches:
            if path[-1] not in aux_2:
                branches.remove(path)

        if flag==1:
          print("\nThis is 'branches' after being restricted by beam_width:", branches)


#####################################################################################################################################
#Responsable: Emiliano
#Función: "Steepest Ascent Hill Climber", es una técnica de búsqueda local que mueve un punto en la dirección del valor 
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
    
    # Se almacenan en una lista todos aquellos nodos que no poseen hijos a fin de evitarlos en la búsqueda del camino a la ciudad destino
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

        for node_weights_list in tree: #comenzamos a iterar en nuestro árbol a fin de encontrar aquella lista que satisfaga que: su primer
        # elemento sea igual al nodo actual. 
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
                        if len(node_weights_list[1]) >= 1:
                            neighbor = node_weights_list[1].pop()
                        else:
                            return "none since the last reached state has no more neighbors" # si no podemos seleccionar otro hijo a explorar (dado que la lista está vacia),
                            # entonces notificamos al usuario que no ha sido posible encontrar un camino al destino, pues el último nodo explorado no cuenta con hijos que nos permitan
                            # alcanzar el nodo final.
                    if flag==1:
                      print(f'\nExploring neighbor: {neighbor}')
                    neighbor_h = heuristic[neighbor[0]]  # we get the neighbor's heuristic value
                    if flag==1:
                      print(
                        f'\nThis is heuristic value of node {neighbor[0]}: {neighbor_h} vs the current heuristic: {current_h}')
                    if neighbor_h < current_h: # hacemos la comparación entre el valor de la heurística del vecino y la de nuestro nodo actual.
                        branch.append(neighbor[0])
                        if branch[-1] == goal:
                            end_time = time.time()
                            tiempo=end_time-start_time
                            return branch, tiempo
                        else:
                            updated_branch = branch.copy() # Al haber obtenido un mejor valor de heurística, agregamos al vecino recientemente analizado a nuestro camino
                            if flag==1:
                              print('\nThis is the updated branch, since a new maximum heuristic value has been found:',
                                  updated_branch)
                            branches.append(updated_branch)
                            if flag==1:
                              print('\nThis is branches: ', branches)
                            break

###########################################################################################################################
#Responsable: Emiliano
#Función: "Stochastic Ascent Hill Climber", busca encontrar la mejor solución a un problema al realizar pequeñas
# modificaciones aleatorias en la solución actual. Cada modificación es evaluada y si mejora la solución, se mantiene, 
# de lo contrario se descarta. El proceso se repite hasta encontrar la mejor solución posible.

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

def Stochastic_Hill_Climber(tree, start, goal, heuristic, flag):
    start_time = time.time()
    nodes_visited = []
    branches = [[start]]
    visited_tuples = []

    while branches:
        if flag==1:
            print('----')
            print('\nBranches available: ', branches)
        branch = branches.pop()
        if flag==1:
            print('\nbranch to explore: ', branch)
            print('\nnodes visited: ', nodes_visited)

        current_node = branch[-1]
        if flag==1:
            print('\ncurrent node ', current_node)

        # checks if the node where we are located is the stop
        if current_node == goal:
            end_time = time.time()
            tiempo=end_time-start_time
            return branch,tiempo 

        if current_node not in nodes_visited:
            nodes_visited.append(current_node)
        if flag==1:
            print('\nThese are the nodes that have been visited:', nodes_visited)

        neighbors_with_h = []
        # we get the neighbors of every node as we did in greedy
        node_neighbors = [node_weights_list[1] for node_weights_list in tree if node_weights_list[0] == current_node]
        if flag==1:
         print(f"\nThese are the neighbors of node {current_node}: ", node_neighbors)

        for neighbors in node_neighbors:
            for neighbor in neighbors:
                value_h = heuristic[neighbor[0]]
                neighbors_with_h.append((neighbor[0], value_h))

        if flag==1:
            print(f"\nThis the the updated list (taking into account heuristic) of neighbors of node {current_node}: ",
              neighbors_with_h)

        neighbors_with_h = Approved_n(neighbors_with_h, tree)  # we make sure that
        if flag==1:
            print("\nThis is the list of approved neighbors (before): ", neighbors_with_h)

        for neighbor in neighbors_with_h:
            if neighbor in visited_tuples:
                neighbors_with_h.remove(neighbor)
        if flag==1:
            print("\nThis is the list of approved neighbors (after): ", neighbors_with_h)

        if len(neighbors_with_h) != 0:
            # the following piece of code turns our hill climber algorithm into a stochastic hill climbing search
            random_number = random.randint(0, len(neighbors_with_h) - 1)  # we obtain a random index
            key_tup = neighbors_with_h.pop(random_number)
            neighbors_with_h = [key_tup]
            if flag==1:
                print('\nThis is the neighbor to be explored:', neighbors_with_h)

            for neighbor in neighbors_with_h:
                if flag==1:
                    print('\nCurrently exploring neighbor:', neighbor)
                if neighbor[0] == goal:  # *
                    branch.append(neighbor[0])

                    end_time = time.time()
                    tiempo=end_time-start_time
                    return branch,tiempo

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
        else:
            key_node = branch.pop(-1)
            key_tuple = (key_node, heuristic[key_node])
            visited_tuples.append(key_tuple)
            if flag==1:
                print('\nThis is the key_tuple: ', key_tuple)
            updated_branch = branch.copy()
            if flag==1:
                print('\nThis is branch after removing the faulty node: ', updated_branch)
            branches.append(updated_branch)
            if flag==1:
                print('\nThis is branches: ', branches)

###########################################################################################
# Responsable: Jimena
# Función: SIMULATED ANNEALING. Requiere de un grafo completamente conectado. A partir de una solución inicial, genera una nueva aleatoria. 
# Calcula la diferencia de costos entre ambas soluciones y decide si aceptar o rechazar la nueva solución según la probabilidad de aceptación 
# y la temperatura. La temperatura va disminuyendo gradualmente. 

# Creamos el objeto 'graph' de la clase DiGraph(). Esto creará un grafo dirigido. 
graph = networkx.DiGraph()

# Incluimos 10 ciudades, todas conectadas entre sí. Utilizamos la heurística dada por Haversine_heuristic().
graph.add_weighted_edges_from({

        ('PUEBLA', 'CIUDAD DE MEXICO', 158),
        ('PUEBLA', 'TOLUCA DE LERDO', 150),
        ('PUEBLA', 'TLAXCALA', 46),
        ('PUEBLA', 'PACHUCA DE SOTO', 130),
        ('PUEBLA', 'CIUDAD ALTAMIRANO', 266),
        ('PUEBLA', 'IZUCAR DE MATAMOROS', 55),
        ('PUEBLA', 'IGUALA', 158),
        ('PUEBLA', 'QUERETARO', 291),
        ('PUEBLA', 'CUERNAVACA', 111),

        ('CIUDAD DE MEXICO', 'PUEBLA', 158),
        ('CIUDAD DE MEXICO', 'TOLUCA DE LERDO', 12),
        ('CIUDAD DE MEXICO', 'TLAXCALA', 133),
        ('CIUDAD DE MEXICO', 'PACHUCA DE SOTO', 121),
        ('CIUDAD DE MEXICO', 'CIUDAD ALTAMIRANO', 153),
        ('CIUDAD DE MEXICO', 'IZUCAR DE MATAMOROS', 155),
        ('CIUDAD DE MEXICO', 'QUERETARO', 158),
        ('CIUDAD DE MEXICO', 'IGUALA', 117),
        ('CIUDAD DE MEXICO', 'CUERNAVACA', 67),

        ('TOLUCA DE LERDO', 'PUEBLA', 150),
        ('TOLUCA DE LERDO', 'CIUDAD DE MEXICO', 12),
        ('TOLUCA DE LERDO', 'TLAXCALA', 70),
        ('TOLUCA DE LERDO', 'PACHUCA DE SOTO', 90),
        ('TOLUCA DE LERDO', 'CIUDAD ALTAMIRANO', 100),
        ('TOLUCA DE LERDO', 'IZUCAR DE MATAMOROS', 90),
        ('TOLUCA DE LERDO', 'IGUALA', 80),
        ('TOLUCA DE LERDO', 'QUERETARO', 90),
        ('TOLUCA DE LERDO', 'CUERNAVACA', 80),

        ('TLAXCALA', 'PUEBLA', 46),
        ('TLAXCALA', 'CIUDAD DE MEXICO', 133),
        ('TLAXCALA', 'TOLUCA DE LERDO', 129),
        ('TLAXCALA', 'PACHUCA DE SOTO', 84),
        ('TLAXCALA', 'CIUDAD ALTAMIRANO', 263),
        ('TLAXCALA', 'IZUCAR DE MATAMOROS', 91),
        ('TLAXCALA', 'IGUALA', 168),
        ('TLAXCALA', 'QUERETARO', 251),
        ('TLAXCALA', 'CUERNAVACA', 106),

        ('PACHUCA DE SOTO', 'PUEBLA', 130),
        ('PACHUCA DE SOTO', 'CIUDAD DE MEXICO', 121),
        ('PACHUCA DE SOTO', 'TOLUCA DE LERDO', 124),
        ('PACHUCA DE SOTO', 'TLAXCALA', 84),
        ('PACHUCA DE SOTO', 'CIUDAD ALTAMIRANO', 274),
        ('PACHUCA DE SOTO', 'IGUALA', 208),
        ('PACHUCA DE SOTO', 'IZUCAR DE MATAMOROS', 168),
        ('PACHUCA DE SOTO', 'QUERETARO', 182),
        ('PACHUCA DE SOTO', 'CUERNAVACA', 138),

        ('CIUDAD ALTAMIRANO', 'PUEBLA', 266),
        ('CIUDAD ALTAMIRANO', 'CIUDAD DE MEXICO', 153),
        ('CIUDAD ALTAMIRANO', 'TOLUCA DE LERDO', 149),
        ('CIUDAD ALTAMIRANO', 'TLAXCALA', 263 ),
        ('CIUDAD ALTAMIRANO', 'PACHUCA DE SOTO', 274),
        ('CIUDAD ALTAMIRANO', 'IZUCAR DE MATAMOROS', 231),
        ('CIUDAD ALTAMIRANO', 'IGUALA', 110),
        ('CIUDAD ALTAMIRANO', 'QUERETARO', 252),
        ('CIUDAD ALTAMIRANO', 'CUERNAVACA', 158),


        ('IZUCAR DE MATAMOROS', 'PUEBLA', 55),
        ('IZUCAR DE MATAMOROS', 'CIUDAD DE MEXICO', 155),
        ('IZUCAR DE MATAMOROS', 'TOLUCA DE LERDO', 144),
        ('IZUCAR DE MATAMOROS', 'TLAXCALA', 91),
        ('IZUCAR DE MATAMOROS', 'PACHUCA DE SOTO', 168),
        ('IZUCAR DE MATAMOROS', 'CIUDAD ALTAMIRANO', 231),
        ('IZUCAR DE MATAMOROS', 'IGUALA', 115),
        ('IZUCAR DE MATAMOROS', 'QUERETARO', 305),
        ('IZUCAR DE MATAMOROS', 'CUERNAVACA', 92),

        ('IGUALA', 'PUEBLA', 158),
        ('IGUALA', 'CIUDAD DE MEXICO', 117),
        ('IGUALA', 'TOLUCA DE LERDO',106 ),
        ('IGUALA', 'TLAXCALA', 168),
        ('IGUALA', 'PACHUCA DE SOTO', 208 ),
        ('IGUALA', 'CIUDAD ALTAMIRANO', 118),
        ('IGUALA', 'IZUCAR DE MATAMOROS', 115),
        ('IGUALA', 'QUERETARO', 270),
        ('IGUALA', 'CUERNAVACA', 71),

        ('QUERETARO', 'PUEBLA', 291),
        ('QUERETARO', 'CIUDAD DE MEXICO', 158),
        ('QUERETARO', 'TOLUCA DE LERDO', 170),
        ('QUERETARO', 'TLAXCALA', 251),
        ('QUERETARO', 'PACHUCA DE SOTO', 182),
        ('QUERETARO', 'CIUDAD ALTAMIRANO', 252),
        ('QUERETARO', 'IZUCAR DE MATAMOROS', 305),
        ('QUERETARO', 'IGUALA', 270),
        ('QUERETARO', 'CUERNAVACA', 223),

        ('CUERNAVACA', 'PUEBLA', 111),
        ('CUERNAVACA', 'CIUDAD DE MEXICO', 67),
        ('CUERNAVACA', 'TOLUCA DE LERDO', 55),
        ('CUERNAVACA', 'TLAXCALA', 106),
        ('CUERNAVACA', 'PACHUCA DE SOTO', 138),
        ('CUERNAVACA', 'CIUDAD ALTAMIRANO', 158),
        ('CUERNAVACA', 'IZUCAR DE MATAMOROS', 92),
        ('CUERNAVACA', 'IGUALA', 71),
        ('CUERNAVACA', 'QUERETARO', 223),
})

# Definimos todas las funciones que nos permitirán hacer el Simulated Annealing:

# 1. generate_initial_solution() recibe nuestro grafo y el punto de partida. 
def generate_initial_solution(graph, start):
    connections = [edges[1] for edges in graph.edges() if edges[0] == start]   # Obtiene los nodos conectados al nodo inicial.
    # print(connections)

    # Añade el nodo inicial al principio y al final de la lista 'connections'.
    connections.insert(0, start) 
    connections.append(start)

    # Verifica que se hayan incluido todos los nodos en la solución. Si falta alguno devuelve la lista vacía (no hubo solución).
    for node in graph.nodes():
        if node not in connections:
            return []

    return connections

# 2. decrease_temperature() recibe la temperatura inicial y el porcentaje de disminución.
def decrease_temperature(temperature, percentage_to_reduce):
    decrease_percentage = 100 * float(percentage_to_reduce) / float(temperature)
    return decrease_percentage

# 3. generate_random_swap_solution() crea una nueva solución a partir de la inicial que recibe.
def generate_random_swap_solution(current_solution):
    # Selecciona dos índices al azar.
    indexes = random.sample(range(1, len(current_solution) - 1), 2)

    # Obtiene los nodos ubicados en esas posiciones.
    value_one = current_solution[indexes[0]]
    value_two = current_solution[indexes[1]]

    # Crea una copia de la solución actual y los intercambia.
    swaped_solution = current_solution.copy()
    swaped_solution[indexes[0]] = value_two
    swaped_solution[indexes[1]] = value_one
    return swaped_solution

# 4. get_solution_cost() recibe la solución.
def get_solution_cost(solution):
    cost = 0

    for i in range(len(solution) - 1):
        cost = cost + graph[solution[i]][solution[i + 1]]["weight"]

    cost = cost + graph[solution[len(solution) - 2]][solution[len(solution) - 1]]["weight"]

    return cost

# Podemos llamar estas funciones para aplicar el algoritmo. Adicionalmente a los parámetros anteriores, recibe la temperatura final.
def simulated_annealing_result(initial_solution, initial_temperature, number_of_iterations, stop_temperature,
                               percentage_to_reduce_temperature, bandera):
    start_time = time.time()
    temperature = initial_temperature
    current_solution = initial_solution

    first_solution_cost = get_solution_cost(current_solution)
    current_solution_cost = 0

    while temperature >= stop_temperature:
        for i in range(number_of_iterations):
            # Genera una nueva solución aleatoria y calcula los costos de ésta y la inicial.
            new_random_solution = generate_random_swap_solution(current_solution)

            if bandera==1:
                print(f"\nLa nueva solución aleatoria es : {new_random_solution}")

            current_solution_cost = get_solution_cost(current_solution)
            new_random_solution_cost = get_solution_cost(new_random_solution)

            if bandera==1:
                print(f"\nEl costo de la solución actual es: {current_solution_cost}")
                print(f"\nEl costo de la nueva solución es: {new_random_solution_cost}")

            # Calcular la diferencia entre los costos de las soluciones.
            diferences_between_costs = current_solution_cost - new_random_solution_cost

            if bandera==1:
                print(f"\nLa diferencia de costos es: {diferences_between_costs}")

            # Si la nueva solución es mejor, se convierte en la solución actual.
            if diferences_between_costs >= 0:
                current_solution = new_random_solution
            else:
                # Si no, calcula una probabilidad de aceptación.
                uniform_random_number = random.uniform(0, 1)
                acceptance_probability = math.exp(diferences_between_costs / temperature)

                if bandera==1:
                    print(f"\nLa probabilidad de aceptación es : {acceptance_probability}")

                # Si se acepta, se convierte en la nueva solución.
                if uniform_random_number <= acceptance_probability:
                    current_solution = new_random_solution

        # Reduce la temperatura para la próxima iteración.
        alpha = decrease_temperature(temperature, percentage_to_reduce_temperature)
        temperature = int(temperature - alpha)
    end_time = time.time()
    final_time = end_time - start_time
    return current_solution, first_solution_cost, current_solution_cost, final_time

# Finalmente, imprimimos la solución final.
def print_simulated_annealing_result(result, initial_solution):
    tuples = []
    for i in range(len(result[0]) - 1):
        tuples.append((result[0][i], result[0][i + 1]))

    simulated_annealing_result = networkx.Graph()

    simulated_annealing_result.add_weighted_edges_from({
        (node_tuple[0], node_tuple[1], graph[node_tuple[0]][node_tuple[1]]["weight"]) for node_tuple in tuples
    })

    print('\nSolución inicial = ', initial_solution)
    print('\nCosto de la solución inicial = ', result[1])
    print('\nSolución del Simulated annealing = ', result[0])
    print('\nCosto de la solución del Simulated annealing = ', result[2])
    print('\nTiempo de ejecución del Simulated annealing= ', result[3])

def main_sim_a():
    banderaSIM=-1
    start = input('\tCiudad de origen: ').upper()
    initial_solution = generate_initial_solution(graph, start)
    initial_temperature = int(input('\tTemperatura inicial (se sugiere 100): '))
    stop_temperature = int(input('\tTemperatura final (se sugiere 0): '))
    number_of_iterations = int(input('\tNo. de iteraciones: '))
    percentage_to_reduce_temperature = int(input('\tPorcentaje de disminución: (se sugiere 2%) '))
    banderaSIM=int(input('Si desea ver la información escriba 1, si no escriba 0: '))

    result = simulated_annealing_result(initial_solution, initial_temperature, number_of_iterations, stop_temperature,
                                        percentage_to_reduce_temperature,banderaSIM)

    print_simulated_annealing_result(result, initial_solution)


##########################################################################################################
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
            print('\nThe Steepest  Hill Climbing exuction time is {}\n'.format(result5[1]))


        if opc==6:
            print("\nStochastic Hill Climbing: ")
            result6 = Steepest_Ascent_Hill_Climber(treecp, start, goal, Goal_hsh, bandera)
            print('\nThe path from {} to {} is {}\n'.format(start, goal, result6[0]))
            print('\nThe Stochastic Hill Climbing algorithm exuction time is {}\n'.format(result6[1]))


        if opc==7:
            print("\nSimulated annealing: ")
            main_sim_a()
        
                  
        if opc == 8:
            print('\nMuchas gracias, hasta luego.')
            break
        else:
            print('Favor de seleccionar una opción válida.')
    

main() 
