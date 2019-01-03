
# Function f = x*x + y - z*z
# f = lambda values: values[0]*values[0] + values[1] - values[2]*values[2]

# Tree generator
import random

from Calculator.AST_Calculator import AST_Calculator
from GA.ASTGeneticAlgorithm import ASTGeneticAlgorithm
from Generator.TreeGenerator import TreeGenerator

terminals = [7, 12, 3, 'x', 'y', 'z']
height = 5
tree_generator = TreeGenerator(terminals, height, random.Random(5))

env = {
    'x': 10,
    'y': -6,
    'z': 10
}

population_size = 16

mutation_rate = 0.05

expected_number = 24

# Calculator
ast_calculator = AST_Calculator(expected_number, env)

# Obtain estadistics from 100 iterations
mean_generations = []
c_last_distance = 0
c_found = 0
for _ in range(100):
    GA = ASTGeneticAlgorithm(tree_generator, population_size, ast_calculator, env, mutation_rate)
    GA.initialize_population()

    generations, chromosome, ga_stats, convergence = GA.genetic_algorithm()

    mean_generations.append(generations)
    if convergence == "last_distance":
        c_last_distance += 1
    else:
        c_found += 1


print(mean_generations)
print(c_last_distance)
print(c_found)
    # print("Generations: {}".format(generations))
    # print("Chromosome: {}".format(chromosome))
    # print("Evaluated chromosome: {}".format(chromosome.eval(env)))

# print("Fitness: {}".format(opti_calculator.calculate_fitness(chromosome)))
#
# expected_sequence = list(map(int8, [chromosome[i:i + 8] for i in range(0, len(chromosome), 8)]))
# print(expected_sequence)
#
#
# lineChart(list(range(generations)), ga_stats["sum"], "Generations", "Total Fitness", "Number of generations vs Total fitness for values {} \n and population size: {}".format(expected_sequence, population_size))
# lineChart(list(range(generations)), ga_stats["mean"], "Generations", "Mean Fitness", "Number of generations vs Mean fitness for values {} \n and population size: {}".format(expected_sequence, population_size))
# lineChart(list(range(generations)), ga_stats["std"], "Generations", "Standard deviation Fitness", "Number of generations vs Std Deviation of fitness for values {} \n and population size: {}".format(expected_sequence, population_size))
# lineChart(list(range(generations)), ga_stats["var"], "Generations", "Var Fitness", "Number of generations vs Variance of fitness for values {} \n and population size: {}".format(expected_sequence, population_size))
# lineChart(list(range(generations)), ga_stats["max"], "Generations", "Var Fitness", "Number of generations vs Highest fitness for values {} \n and population size: {}".format(expected_sequence, population_size))

