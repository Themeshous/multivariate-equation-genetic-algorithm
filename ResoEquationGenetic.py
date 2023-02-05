import random

# Fonction objective
def fitness(chromosome):
    a, b, c, d = chromosome
    return abs((a + 2*b + 3*c + 4*d) - 30)

# Génération initiale de la population
def generate_population(size):
    population = []
    for i in range(size):
        a = random.randint(0, 30)
        b = random.randint(0, 30)
        c = random.randint(0, 30)
        d = random.randint(0, 30)
        population.append([a, b, c, d])
    return population

# Sélection des individus pour la reproduction
def selection(population, fitnesses):
    new_population = []
    for i in range(len(population)):
        parent1 = random.choices(population, weights=fitnesses)[0]
        parent2 = random.choices(population, weights=fitnesses)[0]
        new_population.append(parent1)
    return new_population

# Croisement
def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        gene = random.choice([parent1[i], parent2[i]])
        child.append(gene)
    return child

# Mutation
def mutation(chromosome, probability):
    for i in range(len(chromosome)):
        if random.random() < probability:
            chromosome[i] = random.randint(0, 30)
    return chromosome

# Boucle principale de l'algorithme génétique
def genetic_algorithm(population_size, mutation_probability, max_iterations):
    population = generate_population(population_size)
    for i in range(max_iterations):
        fitnesses = [fitness(chromosome) for chromosome in population]
        population = selection(population, fitnesses)
        new_population = []
        for i in range(int(population_size/2)):
            parent1 = population[i]
            parent2 = population[i+1] if i+1 < len(population) else population[0]
            child = crossover(parent1, parent2)
            child = mutation(child, mutation_probability)
            new_population.append(child)
        population = new_population
    best_chromosome = min(population, key=fitness)
    best_fitness = fitness(best_chromosome)
    return best_chromosome, best_fitness

# Appeler l'algorithme génétique
population_size = 6
mutation_probability = 0.1
max_iterations = 100
best_chromosome, best_fitness = genetic_algorithm(population_size, mutation_probability, max_iterations)
print(best_chromosome, best_fitness)
