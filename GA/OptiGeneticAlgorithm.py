import numpy as np

from GA.GeneticAlgorithm import GeneticAlgorithm
from Individual.Individual import Individual


class OptiGeneticAlgorithm(GeneticAlgorithm):

    def __init__(self, *args, **kwargs):
        super(OptiGeneticAlgorithm, self).__init__(*args, **kwargs)


    # Override of father reproduce, to reproduce by chunks of data
    def reproduce(self, individual1, individual2):

        # Create new gen, for each 8bit chunk
        variables_individual1 = [individual1.chromosome[i:i + 8] for i in range(0, len(individual1.chromosome), 8)]
        variables_individual2 = [individual2.chromosome[i:i + 8] for i in range(0, len(individual2.chromosome), 8)]

        new_chromosome = ""

        for var1, var2 in zip(variables_individual1, variables_individual2):
            mixing_point = self.rand.randint(0, len(var1))
            new_variable = var2[:mixing_point] + var1[mixing_point:]

            # Mutate based of mutation_rate
            if self.mutation_rate > self.rand.random():
                # new_gen = list(map(lambda g: self.mutate(g), new_gen))
                new_variable = self.mutate(new_variable)

            new_chromosome += new_variable

        return Individual(new_chromosome)


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
                generation_count -= 1
            else:
                generation_count = default
            generations += 1
            # print(generations)


        return generations, self.population[0].chromosome, total_stats


