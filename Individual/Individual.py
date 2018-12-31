from functools import reduce


class Individual:

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.score = 0

    def evaluate_fitness(self, fitness_calculator):
        # diff_list = map((lambda x: 1 if x[0] == x[1] else 0), list(zip(self.chromosome, expected_sequence)))
        # self.score = reduce((lambda x, y: x + y), diff_list)
        self.score = fitness_calculator.calculate_fitness(self.chromosome)
        return self.score

# ind = Individual("00100")
# print(ind.evaluate_fitness("00100"))
