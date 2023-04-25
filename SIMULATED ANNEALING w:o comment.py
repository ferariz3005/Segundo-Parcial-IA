# SIMULATED ANNEALING.


import networkx
import random, math
#------------------------------------------------------------------------------------
graph = networkx.DiGraph()

# We create a specific graph for the simulated annealing function. 
# We create our graph as an object from the class DiGraph(), which is a Directed Graph. We've exported this from the 
#library networkx. This graph has certain connections given in class, we've added others in order for it to be
#completely connected. We need this kind of graph to use 'Simulated Annealing'.

graph.add_weighted_edges_from({

        ('PUEBLA', 'CIUDAD DE MEXICO', 90),
        ('PUEBLA', 'TOLUCA DE LERDO', 90),
        ('PUEBLA', 'TLAXCALA', 70),
        ('PUEBLA', 'PACHUCA DE SOTO', 90),
        ('PUEBLA', 'CIUDAD ALTAMIRANO', 90),
        ('PUEBLA', 'IZUCAR DE MATAMOROS', 90),
        ('PUEBLA', 'IGUALA', 90),
        ('PUEBLA', 'QUERETARO', 100),
        ('PUEBLA', 'CUERNAVACA', 100),

        ('CIUDAD DE MEXICO', 'PUEBLA', 90),
        ('CIUDAD DE MEXICO', 'TOLUCA DE LERDO', 110),
        ('CIUDAD DE MEXICO', 'TLAXCALA', 100),
        ('CIUDAD DE MEXICO', 'PACHUCA DE SOTO', 100),
        ('CIUDAD DE MEXICO', 'CIUDAD ALTAMIRANO', 100),
        ('CIUDAD DE MEXICO', 'IZUCAR DE MATAMOROS', 110),
        ('CIUDAD DE MEXICO', 'QUERETARO', 90),
        ('CIUDAD DE MEXICO', 'IGUALA', 110),
        ('CIUDAD DE MEXICO', 'CUERNAVACA', 100),

        ('TOLUCA DE LERDO', 'PUEBLA', 90),
        ('TOLUCA DE LERDO', 'CIUDAD DE MEXICO', 110),
        ('TOLUCA DE LERDO', 'TLAXCALA', 70),
        ('TOLUCA DE LERDO', 'PACHUCA DE SOTO', 90),
        ('TOLUCA DE LERDO', 'CIUDAD ALTAMIRANO', 100),
        ('TOLUCA DE LERDO', 'IZUCAR DE MATAMOROS', 90),
        ('TOLUCA DE LERDO', 'IGUALA', 80),
        ('TOLUCA DE LERDO', 'QUERETARO', 90),
        ('TOLUCA DE LERDO', 'CUERNAVACA', 80),

        ('TLAXCALA', 'PUEBLA', 70),
        ('TLAXCALA', 'CIUDAD DE MEXICO', 100),
        ('TLAXCALA', 'TOLUCA DE LERDO', 70),
        ('TLAXCALA', 'PACHUCA DE SOTO', 70),
        ('TLAXCALA', 'CIUDAD ALTAMIRANO', 90),
        ('TLAXCALA', 'IZUCAR DE MATAMOROS', 100),
        ('TLAXCALA', 'IGUALA', 90),
        ('TLAXCALA', 'QUERETARO', 90),
        ('TLAXCALA', 'CUERNAVACA', 90),

        ('PACHUCA DE SOTO', 'PUEBLA', 90),
        ('PACHUCA DE SOTO', 'CIUDAD DE MEXICO', 100),
        ('PACHUCA DE SOTO', 'TOLUCA DE LERDO', 90),
        ('PACHUCA DE SOTO', 'TLAXCALA', 70),
        ('PACHUCA DE SOTO', 'CIUDAD ALTAMIRANO', 80),
        ('PACHUCA DE SOTO', 'IGUALA', 80),
        ('PACHUCA DE SOTO', 'IZUCAR DE MATAMOROS', 80),
        ('PACHUCA DE SOTO', 'QUERETARO', 80),
        ('PACHUCA DE SOTO', 'CUERNAVACA', 90),

        ('CIUDAD ALTAMIRANO', 'PUEBLA', 90),
        ('CIUDAD ALTAMIRANO', 'CIUDAD DE MEXICO', 100),
        ('CIUDAD ALTAMIRANO', 'TOLUCA DE LERDO', 100),
        ('CIUDAD ALTAMIRANO', 'TLAXCALA', 90 ),
        ('CIUDAD ALTAMIRANO', 'PACHUCA DE SOTO', 80),
        ('CIUDAD ALTAMIRANO', 'IZUCAR DE MATAMOROS', 90),
        ('CIUDAD ALTAMIRANO', 'IGUALA', 110),
        ('CIUDAD ALTAMIRANO', 'QUERETARO', 100),
        ('CIUDAD ALTAMIRANO', 'CUERNAVACA', 100),


        ('IZUCAR DE MATAMOROS', 'PUEBLA', 90),
        ('IZUCAR DE MATAMOROS', 'CIUDAD DE MEXICO', 110),
        ('IZUCAR DE MATAMOROS', 'TOLUCA DE LERDO', 100),
        ('IZUCAR DE MATAMOROS', 'TLAXCALA', 100),
        ('IZUCAR DE MATAMOROS', 'PACHUCA DE SOTO', 70),
        ('IZUCAR DE MATAMOROS', 'CIUDAD ALTAMIRANO', 80),
        ('IZUCAR DE MATAMOROS', 'IGUALA', 80),
        ('IZUCAR DE MATAMOROS', 'QUERETARO', 90),
        ('IZUCAR DE MATAMOROS', 'CUERNAVACA', 100),

        ('IGUALA', 'PUEBLA', 90),
        ('IGUALA', 'CIUDAD DE MEXICO', 110),
        ('IGUALA', 'TOLUCA DE LERDO',80 ),
        ('IGUALA', 'TLAXCALA', 90),
        ('IGUALA', 'PACHUCA DE SOTO', 80 ),
        ('IGUALA', 'CIUDAD ALTAMIRANO', 110),
        ('IGUALA', 'IZUCAR DE MATAMOROS', 80),
        ('IGUALA', 'QUERETARO', 100),
        ('IGUALA', 'CUERNAVACA', 100),

        ('QUERETARO', 'PUEBLA', 100),
        ('QUERETARO', 'CIUDAD DE MEXICO', 90),
        ('QUERETARO', 'TOLUCA DE LERDO', 90),
        ('QUERETARO', 'TLAXCALA', 90),
        ('QUERETARO', 'PACHUCA DE SOTO', 80),
        ('QUERETARO', 'CIUDAD ALTAMIRANO', 100),
        ('QUERETARO', 'IZUCAR DE MATAMOROS', 90),
        ('QUERETARO', 'IGUALA', 100),
        ('QUERETARO', 'CUERNAVACA', 110),

        ('CUERNAVACA', 'PUEBLA', 100),
        ('CUERNAVACA', 'CIUDAD DE MEXICO', 100),
        ('CUERNAVACA', 'TOLUCA DE LERDO', 80),
        ('CUERNAVACA', 'TLAXCALA', 90),
        ('CUERNAVACA', 'PACHUCA DE SOTO', 90),
        ('CUERNAVACA', 'CIUDAD ALTAMIRANO', 100),
        ('CUERNAVACA', 'IZUCAR DE MATAMOROS', 100),
        ('CUERNAVACA', 'IGUALA', 100),
        ('CUERNAVACA', 'QUERETARO', 110),
})

#print(graph.nodes())
#print(graph.edges())

#We generate a random initial solution.
def generate_initial_solution(graph, start):
    connections = [edges[1] for edges in graph.edges() if edges[0] == start]
    print(connections)
    connections.insert(0, start)
    connections.append(start)

    for node in graph.nodes():
        if node not in connections:
            return []

    return connections

#print(generate_initial_solution(graph, 'IGUALA'))


#We define our temperature function.
def decrease_temperature(temperature, percentage_to_reduce):
    decrease_percentage = 100 * float(percentage_to_reduce) / float(temperature)
    return decrease_percentage

#--
def generate_random_swap_solution(current_solution):
    indexes = random.sample(range(1, len(current_solution) - 1), 2)
    value_one = current_solution[indexes[0]]
    value_two = current_solution[indexes[1]]
    swaped_solution = current_solution.copy()
    swaped_solution[indexes[0]] = value_two
    swaped_solution[indexes[1]] = value_one
    return swaped_solution

#--
def get_solution_cost(solution):
    cost = 0

    for i in range(len(solution) - 1):
        cost = cost + graph[solution[i]][solution[i + 1]]["weight"]

    cost = cost + graph[solution[len(solution) - 2]][solution[len(solution) - 1]]["weight"]

    return cost

#--
def simulated_annealing_result(initial_solution, initial_temperature, number_of_iterations, stop_temperature,
                               percentage_to_reduce_temperature):
    temperature = initial_temperature
    current_solution = initial_solution

    first_solution_cost = get_solution_cost(current_solution)
    current_solution_cost = 0

    while temperature >= stop_temperature:
        for i in range(number_of_iterations):
            new_random_solution = generate_random_swap_solution(current_solution)
            # print(new_random_solution)

            current_solution_cost = get_solution_cost(current_solution)
            new_random_solution_cost = get_solution_cost(new_random_solution)
            # print(current_solution_cost)
            # print(new_random_solution_cost)

            diferences_between_costs = current_solution_cost - new_random_solution_cost
            # print(diferences_between_costs)

            if diferences_between_costs >= 0:
                current_solution = new_random_solution
            else:
                uniform_random_number = random.uniform(0, 1)
                # print(uniform_random_number)

                acceptance_probability = math.exp(diferences_between_costs / temperature)
                # print(acceptance_probability)

                if uniform_random_number <= acceptance_probability:
                    current_solution = new_random_solution

        alpha = decrease_temperature(temperature, percentage_to_reduce_temperature)
        temperature = int(temperature - alpha)

    return current_solution, first_solution_cost, current_solution_cost

#--
def print_simulated_annealing_result(result, initial_solution):
    tuples = []
    for i in range(len(result[0]) - 1):
        tuples.append((result[0][i], result[0][i + 1]))

    simulated_annealing_result = networkx.Graph()

    simulated_annealing_result.add_weighted_edges_from({
        (node_tuple[0], node_tuple[1], graph[node_tuple[0]][node_tuple[1]]["weight"]) for node_tuple in tuples
    })

    print('\nInitial solution = ', initial_solution)
    print('\nInitial solution cost = ', result[1])
    print('\nSimulated annealing solution = ', result[0])
    print('\nSimulated annealing solution cost = ', result[2])

def main():
    start = input('Start search from: ')
    initial_solution = generate_initial_solution(graph, start)
    initial_temperature = 100
    stop_temperature = 0
    number_of_iterations = 5
    percentage_to_reduce_temperature = 2

    result = simulated_annealing_result(initial_solution, initial_temperature, number_of_iterations, stop_temperature,
                                        percentage_to_reduce_temperature)

    print_simulated_annealing_result(result, initial_solution)


main()