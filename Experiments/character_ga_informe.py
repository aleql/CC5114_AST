import random

import numpy as np

from Calculator.Seq_Calculator import Seq_Calculator
from Charts import lineChart
from GA.GeneticAlgorithm import GeneticAlgorithm
from Generator.Generator import Generator


binary_stats = {}
binary_stats["mean_generations"] = []
binary_stats["sequence_length"] = []
binary_stats["errors"] = []


for l in range(10, 50, 5):
    mean_generations = []
    population_size = int(l / 2)
    error = 0

    for _ in range(10):
        character_generator = Generator(list("abcdefghijklmnñopqrstuvwxyz"), l)
        expected_sequence = character_generator.generate_sequence()

        mutation_rate = 0.1

        rand = random.Random()

        # Calculator
        calculator = Seq_Calculator(expected_sequence)

        GA = GeneticAlgorithm(character_generator, population_size, calculator, mutation_rate, rand)
        GA.initialize_population()

        generations, chromosome, ga_stats = GA.genetic_algorithm()
        # print("Generations: {}".format(generations))
        # print("Chromosome: {}".format(chromosome))
        if chromosome != expected_sequence:
            error += 1
            print(chromosome)

        mean_generations.append(generations)

    print(l)
    binary_stats["sequence_length"].append(l)
    binary_stats["mean_generations"].append(np.mean(mean_generations))
    binary_stats["errors"].append(error)

print(binary_stats["sequence_length"])
print(binary_stats["mean_generations"])
print(binary_stats["errors"])
# lineChart(list(range(generations)), ga_stats["sum"], "Generations", "Total Fitness", "Number of generations vs Total fitness for binary string {} \n and population size: {}".format(expected_sequence, population_size))
lineChart(binary_stats["sequence_length"], binary_stats["mean_generations"], "Sequence length", "number of generations", "Sequence length vs Number of generations for character strings")
lineChart(binary_stats["sequence_length"], binary_stats["errors"], "Sequence length", "Errors", "Sequence length vs Number of errors per prediction for character strings")


# lineChart(list(range(generations)), binary_stats["std"], "Generations", "Standard deviation Fitness", "Number of generations vs Std Deviation of fitness for binary strings \n and population size: {}".format(expected_sequence, population_size))
# lineChart(list(range(generations)), binary_stats["var"], "Generations", "Var Fitness", "Number of generations vs Variance of fitness for binary strings \n and population size: {}".format(expected_sequence, population_size))
# lineChart(list(range(generations)), binary_stats["max"], "Generations", "Maximun Fitness", "Number of generations vs Highest individual fitness for binary strings \n and population size: {}".format(expected_sequence, population_size))
#
