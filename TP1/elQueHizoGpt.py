import random

def fitness_function(x, coef):
    return (x / coef) ** 2

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(individual):
    mutation_point = random.randint(0, len(individual) - 1)
    mutated_individual = individual[:mutation_point] + str(1 - int(individual[mutation_point])) + individual[mutation_point + 1:]
    return mutated_individual

def generate_initial_population(population_size, chromosome_length):
    population = []
    for _ in range(population_size):
        individual = ''.join(str(random.randint(0, 1)) for _ in range(chromosome_length))
        population.append(individual)
    return population

def select_parent(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_probability = [fitness / total_fitness for fitness in fitness_values]
    return random.choices(population, weights=selection_probability)[0]

def genetic_algorithm():
    coef = 2 ** 30 - 1
    population_size = 10
    chromosome_length = 30
    crossover_probability = 0.75
    mutation_probability = 0.05
    generations = 20

    population = generate_initial_population(population_size, chromosome_length)

    for _ in range(generations):
        fitness_values = [fitness_function(int(individual, 2), coef) for individual in population]

        new_population = []

        for _ in range(population_size // 2):
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population, fitness_values)

            if random.random() < crossover_probability:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            if random.random() < mutation_probability:
                child1 = mutation(child1)
            if random.random() < mutation_probability:
                child2 = mutation(child2)

            new_population.extend([child1, child2])

        population = new_population

    best_individual = max(population, key=lambda individual: fitness_function(int(individual, 2), coef))
    best_fitness = fitness_function(int(best_individual, 2), coef)

    print("Best Individual:", best_individual)
    print("Best Fitness:", best_fitness)

genetic_algorithm()
