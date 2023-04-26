
# SIMULATED ANNEALING.

# Importamos la librería networkx para poder trabajar con grafos.
import networkx
import random, math
from math import radians, cos, sin, asin, sqrt
import time

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

#print(graph.nodes())
#print(graph.edges())

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
    print('\nCosto de la solución innicial = ', result[1])
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


main_sim_a()