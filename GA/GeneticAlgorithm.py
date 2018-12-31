import random

import itertools
from functools import reduce

import numpy as np

from Individual.Individual import Individual


class GeneticAlgorithm:

    def __init__(self, generator, population_size, fitness_calculator, mutation_rate=0.1,
                 rand=random.Random(9001)):
        self.population = []
        self.generator = generator
        self.fitness_calculator = fitness_calculator
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.rand = rand

    # Initialize a new population of given size
    def initialize_population(self):
        for _ in range(self.population_size):
            new_individual = Individual(self.generator.generate_sequence())
            self.population.append(new_individual)

    # Select an individual from a population given a number of iterations
    def tournament_selection(self):
        best = None
        for i in range(self.population_size):
            individual = self.rand.choice(self.population)
            if best is None or individual.score > best.score:
                best = individual
        return best

    # For a chromosome, mutate, changes randomly one gen of the chromosome.
    def mutate(self, chromosome):
        mutation_index = self.rand.randint(0, len(chromosome) - 1)

        # Mutate a single random chosen chromosome
        mutated_chromosome = list(chromosome)
        mutated_chromosome[mutation_index] = self.generator.generate_single_gen()
        return ''.join(mutated_chromosome)


    # Produce a new individual given two parent indivuals,
    # The new inidivual is mutated given a mutation_rate
    def reproduce(self, individual1, individual2):

        # Create new gen
        mixing_point = self.rand.randint(0, len(individual1.chromosome))
        new_chromosome = individual2.chromosome[:mixing_point] + individual1.chromosome[mixing_point:]

        # Mutate based of mutation_rate
        if self.mutation_rate > self.rand.random():
            # new_gen = list(map(lambda g: self.mutate(g), new_gen))
            new_chromosome = self.mutate(new_chromosome)

        return Individual(new_chromosome)

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

        # Check if all the individuals in the list have the same chromosome
        def all_same(items):
            return all( i.chromosome == items[0].chromosome for i in items)

        # Obtain population fitness
        def pop_fitness(population):
            fitness = list(map(lambda i: i.score, population))
            return fitness


        # Default generation count
        default = generation_count

        # List for the fitness by generation
        total_stats = {}
        total_stats["mean"] = []
        total_stats["sum"] = []
        total_stats["std"] = []
        total_stats["var"] = []
        total_stats["max"] = []
        # generation_fitness.append(pop_fitness(self.population))


        # Algorithm
        generations = 0
        while generation_count > 0:

            # Evaluate population to obtain stats
            self.evaluate_population()
            generation_fitness = pop_fitness(self.population)
            total_stats["mean"].append(np.mean(generation_fitness))
            total_stats["sum"].append(np.sum(generation_fitness))
            total_stats["std"].append(np.std(generation_fitness))
            total_stats["var"].append(np.var(generation_fitness))
            total_stats["max"].append(np.amax(generation_fitness))

            self.new_generation()


            # pop = ""
            # for i in self.population:
            #     pop += str(i.chromosome) + " "  + "/" + str(i.score) + " "
            # print(" Population: " + str(generations) + " / " + pop)

            if all_same(self.population):
                self.population[0].evaluate_fitness(self.fitness_calculator)
                if self.population[0].score == len(self.population[0].chromosome):
                    generation_count -= 1
            else:
                generation_count = default
            generations += 1
            # print(generations)


        return generations, self.population[0].chromosome, total_stats





