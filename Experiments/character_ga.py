
from Calculator.Seq_Calculator import Seq_Calculator
from Charts import lineChart
from GA.GeneticAlgorithm import GeneticAlgorithm
from Generator.Generator import Generator

character_generator = Generator(list("abcdefghijklmnñopqrstuvwxyz"), 9)

#
expected_sequence = "comicsans"

population_size = 12

mutation_rate = 0.1

# Calculator
calculator = Seq_Calculator(expected_sequence)

GA = GeneticAlgorithm(character_generator, population_size, calculator, mutation_rate)
GA.initialize_population()

generations, chromosome, ga_stats = GA.genetic_algorithm()
print("Generations: {}".format(generations))
print("Chromosome: {}".format(chromosome))
# print("ga_stats: {}".format(ga_stats))


# lineChart(list(range(generations)), ga_stats["sum"], "Generations", "Total Fitness", "Number of generations vs Total fitness \n for character string {} and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["mean"], "Generations", "Mean Fitness", "Number of generations vs Mean fitness \n for character string {} and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["std"], "Generations", "Standard deviation Fitness", "Number of generations vs Std Deviation of fitness \n for character string {} and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["var"], "Generations", "Var Fitness", "Number of generations vs Variance of fitness \n for character string {} and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["max"], "Generations", "Var Fitness", "Number of generations vs Highest individual fitness \n for character string {} and population size: {}".format(expected_sequence, population_size))

