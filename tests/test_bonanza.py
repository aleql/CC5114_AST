

# Create new generator
# 0,1 5 lenght sequence generator
from Calculator.Seq_Calculator import Seq_Calculator
from GA.GeneticAlgorithm import GeneticAlgorithm
from Generator.Generator import Generator

generator = Generator(list("abcdefghijklmnñopqrstuvwxyz"), 10)


# diff_list = map((lambda x: 1 if x[0] == x[1] else 0), list(zip(self.chromosome, expected_sequence)))
# self.score = reduce((lambda x, y: x + y), diff_list)


# generator = Generator(['0', '1'], 5)
# print(generator.generate_sequence())
# print(generator.generate_single_gen())

# Create an individual and check fitness
# test_individual = Individual(generator.generate_sequence())
# print(test_individual.evaluate_fitness("bjcri"))

# Generate population

# Calculator
calculator = Seq_Calculator("murcielago")

GA = GeneticAlgorithm(generator, 16, calculator)
GA.initialize_population()

print(GA.genetic_algorithm())
# pop = ""
# for i in GA.population:
#     pop += str(i.chromosome) # + "/" + str(i.score) + " "
# print("Initial populi: ")
# print(pop)
# print()
#
# last = None
# for _ in range(100):
#     GA.new_generation()
#     pop = ""
#     for i in GA.population:
#         pop += str(i.chromosome) # + "/" + str(i.score) + " "
#     print("New populi: ")
#     print(pop)
#     # last = pop
#     print()
#
# print("end")
# print(last)

