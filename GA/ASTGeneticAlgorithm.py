import random

import itertools

import numpy as np

from AST.OpTree import OpTree
from Individual.Individual import Individual


class ASTGeneticAlgorithm:

    def __init__(self, generator, population_size, fitness_calculator, environment, mutation_rate=0.1,
                 rand=random.Random(9001)):
        # GA parameters
        self.population = []
        self.generator = generator
        self.fitness_calculator = fitness_calculator
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.rand = rand
        # AST parameters
        self.environment = environment
        self.operations = generator.operations
        self.terminals = generator.terminals
        self.height = generator.height

    # Initialize a new population of given size
    def initialize_population(self):
        for _ in range(self.population_size):
            new_individual = Individual(self.generator.generate_tree(self.height))
            self.population.append(new_individual)

    # Select an individual from a population given a number of iterations
    def tournament_selection(self):
        best = None
        for i in range(self.population_size):
            individual = self.rand.choice(self.population)
            if best is None or individual.score > best.score:
                best = individual
        return best

    # Produce a new individual given two parent indivuals,
    # The new inidivual is mutated given a mutation_rate
    def reproduce(self, individualA, individualB):

        # Obtain trees
        nodeA = individualA.chromosome
        nodeB = individualB.chromosome

        #
        # Create new tree, as the best combination of the individuals
        # Generate all combinations between two nodes and operations
        combinations = [self.operations, nodeA.toList(), nodeB.toList()]
        combinations_perm = [self.operations, nodeB.toList(), nodeA.toList()]
        combinations = itertools.product(*combinations)
        combinations_perm = itertools.product(*combinations_perm)

        combinations = itertools.chain(combinations, combinations_perm)

        # Find the best combination
        best_tree = None
        best_score = None
        for combination in combinations:
            candidate_tree = OpTree(combination[0], combination[1], combination[2])

            # If candidate height is higher that the allowed one, then is skipped
            if candidate_tree.height() > self.generator.height:
                continue

            # Obtain fitness
            candidate_score = self.fitness_calculator.calculate_fitness(candidate_tree)

            # New best candidate
            if best_score is None or candidate_score > best_score:
                best_score = candidate_score
                best_tree = candidate_tree

        # Mutate based of mutation_rate
        best_tree = self.generator.mutate_tree(best_tree, self.mutation_rate)

        return Individual(best_tree)

    # Generate a new population in a round robin permutation
    def generate_population(self, mating_pool):
        new_generation = []

        # Border case, only one individual for reproduction
        if len(mating_pool) == 1:
            while len(new_generation) < self.population_size:
                new_generation.append(self.reproduce(mating_pool[0], mating_pool[0]))
            return new_generation

        # More than one inividual
        cycle_combinations = itertools.cycle(list(itertools.combinations(mating_pool, 2)))
        while len(new_generation) < self.population_size:
            mating_individuals = next(cycle_combinations)
            new_generation.append(self.reproduce(mating_individuals[0], mating_individuals[1]))
        return new_generation

    # Generate new population from the best individuals in a generation choosen via tournament selection.
    def new_generation(self):
        # Generate mating pool, size = 1/4 size population
        mating_pool_size = int(self.population_size/4)
        mating_pool = [self.tournament_selection() for _ in range(mating_pool_size)]

        # Generate a new population
        new_generation = self.generate_population(mating_pool)

        # replace population
        self.population = new_generation

    # Calculates the fitness of each individual of the population
    def evaluate_population(self):
        for individual in self.population:
            individual.evaluate_fitness(self.fitness_calculator)

    # Solution is found when the population is the same generetaion count times
    def genetic_algorithm(self, generation_count=3):

        # Obtain the chromosome of highest score in a population
        def best_tree(individuals):
            best_tree = None
            best_score = None
            for i in individuals:
                # print(i.score)
                if best_score is None or i.score > best_score:
                    best_score = i.score
                    best_tree = i.chromosome
            return best_tree


        # Obtain population fitness
        def pop_fitness(population):
            fitness = list(map(lambda i: i.score, population))
            return fitness


        # List for the fitness by generation
        total_stats = {}
        total_stats["mean"] = []
        total_stats["sum"] = []
        total_stats["std"] = []
        total_stats["var"] = []
        total_stats["max"] = []

        # Algorithm
        generations = 0
        found = False

        # Convergence by 5 generations with same distance
        generation_default = 5
        generation_count = 5
        last_distance = None
        while not found and generation_count != 0:

            # Evaluate population to obtain stats
            self.evaluate_population()
            generation_fitness = pop_fitness(self.population)

            maximum_fitness = np.amax(generation_fitness)

            total_stats["mean"].append(np.mean(generation_fitness))
            total_stats["sum"].append(np.sum(generation_fitness))
            total_stats["std"].append(np.std(generation_fitness))
            total_stats["var"].append(np.var(generation_fitness))
            total_stats["max"].append(maximum_fitness)

            print("GENERATIONS: {} || MAX: {}".format(generations, np.amax(generation_fitness)))

            if maximum_fitness == 0:
                found = True

            else:
                if maximum_fitness == last_distance:
                    generation_count -= 1
                else:
                    # Reset counter
                    last_distance = maximum_fitness
                    generation_count = generation_default

                generations += 1

                # New generation
                self.new_generation()

        # Converge criteria
        if generation_count == 0:
            print("Converge by last distance")
        else:
            print("Converge by found")

        return generations, best_tree(self.population), total_stats



            # pop = ""
            # for i in self.population:
            #     pop += str(i.chromosome) + " "  + "/" + str(i.score) + " "
            # print(" Population: " + str(generations) + " / " + pop)

            # if maximum_fitness == 0:
            #     found = True
            # else:
                # generation_count = default


            # print(generations)


        # return generations, best_tree(self.population), total_stats





