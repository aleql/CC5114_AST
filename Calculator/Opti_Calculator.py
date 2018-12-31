
from Calculator.Fitness_Calculator import Fitness_Calculator
from Calculator.Utils import int8


class Opti_Calculator(Fitness_Calculator):

    def __init__(self, function):

        def function_opti_fitness(chromosome):

            # Obtain each of the binary and turn to int.
            variables = list(map(int8, [chromosome[i:i + 8] for i in range(0, len(chromosome), 8)]))
            score = (function(variables))
            return score

        super().__init__(function_opti_fitness)
