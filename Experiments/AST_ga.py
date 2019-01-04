
import random

import numpy as np

from AST.Charts.Charts import lineChart
from Calculator.AST_Calculator import AST_Calculator
from GA.ASTGeneticAlgorithm import ASTGeneticAlgorithm
from Generator.TreeGenerator import TreeGenerator


# Mean fitness by generation
convergence = "last_distance"
while convergence != "found":
    terminals = [19, 7, 40, 3]
    height = 8
    tree_generator = TreeGenerator(terminals, height, random.Random(5))

    env = {}

    population_size = 128

    mutation_rate = 0.05

    expected_number = 147

    # Calculator
    ast_calculator = AST_Calculator(expected_number, env)

    GA = ASTGeneticAlgorithm(tree_generator, population_size, ast_calculator, env, mutation_rate)
    GA.initialize_population()

    generations, chromosome, ga_stats, convergence = GA.genetic_algorithm()

print("Generations: {}".format(generations))
print("Convergence by : {}".format(convergence))
print("Chromosome: {}".format(chromosome))
print("Evaluated chromosome: {}".format(chromosome.eval(env)))

print(len(ga_stats["max"]))
print(ga_stats["max"])

lineChart(list(range(generations)), ga_stats["max"], "Generations", "Max Fitness", "Number of generations vs Max fitness \n for population size: {} and height: {}".format(population_size, height))
lineChart(list(range(generations)), ga_stats["mean"], "Generations", "Mean Fitness", "Number of generations vs Mean fitness \n for population size: {} and height: {}".format(population_size, height))
lineChart(list(range(generations)), ga_stats["std"], "Generations", "Std of Fitness", "Number of generations vs Std of fitness \n for population size: {} and height: {}".format(population_size, height))
lineChart(list(range(generations)), ga_stats["var"], "Generations", "Variance of Fitness", "Number of generations vs Variance of fitness \n for population size: {} and height: {}".format(population_size, height))


# Height vs Convergence:

covergence_per_height = []
heights = list(range(5, 11))

iterations = 10
for height in heights:
    mean_convergence = []
    print("height: {}".format(height))
    for _ in range(iterations):
        terminals = [19, 7, 40, 3]
        tree_generator = TreeGenerator(terminals, height, random.Random(5))

        env = {}

        population_size = 128

        mutation_rate = 0.05

        expected_number = 147

        # Calculator
        ast_calculator = AST_Calculator(expected_number, env)

        GA = ASTGeneticAlgorithm(tree_generator, population_size, ast_calculator, env, mutation_rate)
        GA.initialize_population()

        generations, chromosome, ga_stats, convergence = GA.genetic_algorithm()

        mean_convergence.append(generations)

    covergence_per_height.append(np.mean(mean_convergence))

print(heights)
print(covergence_per_height)
lineChart(heights, covergence_per_height, "AST height", "Generations to converge", "AST max height vs Generations to converge")


#Population vs Convergence:

covergence_per_height = []
populations = [2**x for x in range(3, 10)]

iterations = 10
for population in populations:
    mean_convergence = []
    print(population)
    for _ in range(iterations):
        height = 8
        terminals = [19, 7, 40, 3]
        tree_generator = TreeGenerator(terminals, height, random.Random(5))

        env = {}

        population_size = population

        mutation_rate = 0.05

        expected_number = 147

        # Calculator
        ast_calculator = AST_Calculator(expected_number, env)

        GA = ASTGeneticAlgorithm(tree_generator, population_size, ast_calculator, env, mutation_rate)
        GA.initialize_population()

        generations, chromosome, ga_stats, convergence = GA.genetic_algorithm()

        mean_convergence.append(generations)

    covergence_per_height.append(np.mean(mean_convergence))

print(populations)
print(covergence_per_height)
lineChart(populations, covergence_per_height, "Population sizes", "Generations to converge", "Population sizes vs Generations to converge \n for max height 5")

