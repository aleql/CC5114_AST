from Calculator.Opti_Calculator import Opti_Calculator
from Calculator.Utils import int8
from Charts import lineChart
from GA.OptiGeneticAlgorithm import OptiGeneticAlgorithm
from Generator.Generator import Generator

# Function f = x*x + y - z*z
f = lambda values: values[0]*values[0] + values[1] - values[2]*values[2]

opti_generator = Generator(list("01"), 24)

population_size = 16

mutation_rate = 0.1

# Calculator
opti_calculator = Opti_Calculator(f)

GA = OptiGeneticAlgorithm(opti_generator, 12, opti_calculator, mutation_rate)
GA.initialize_population()

generations, chromosome, ga_stats = GA.genetic_algorithm()
print("Generations: {}".format(generations))
print("Chromosome: {}".format(chromosome))

print("Fitness: {}".format(opti_calculator.calculate_fitness(chromosome)))

expected_sequence = list(map(int8, [chromosome[i:i + 8] for i in range(0, len(chromosome), 8)]))
print(expected_sequence)


lineChart(list(range(generations)), ga_stats["sum"], "Generations", "Total Fitness", "Number of generations vs Total fitness for values {} \n and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["mean"], "Generations", "Mean Fitness", "Number of generations vs Mean fitness for values {} \n and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["std"], "Generations", "Standard deviation Fitness", "Number of generations vs Std Deviation of fitness for values {} \n and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["var"], "Generations", "Var Fitness", "Number of generations vs Variance of fitness for values {} \n and population size: {}".format(expected_sequence, population_size))
lineChart(list(range(generations)), ga_stats["max"], "Generations", "Var Fitness", "Number of generations vs Highest fitness for values {} \n and population size: {}".format(expected_sequence, population_size))

