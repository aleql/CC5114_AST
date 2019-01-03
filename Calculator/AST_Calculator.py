
from Calculator.Fitness_Calculator import Fitness_Calculator


class AST_Calculator(Fitness_Calculator):

    def __init__(self, expected_number, environment):

        self.expected_number = expected_number
        self.environment = environment

        # The fitness function is the distance between the expected number and the evaluation of the tree
        def function_AST_fitness(node):

            # Negative distance to the expected number}
            # print(str(node))
            score = - abs(node.eval(environment) - self.expected_number)
            return score

        super().__init__(function_AST_fitness)
