
from Calculator.Fitness_Calculator import Fitness_Calculator


class F_AST_Calculator(Fitness_Calculator):

    def __init__(self, environment, var_range, function, variable):

        self.environment = environment
        self.var_range = var_range
        self.function = function

        # The fitness function is the distance between the expected number and the evaluation of the tree
        def function_F_AST_fitness(node):

            # Negative distance to the expected number}
            # print(str(node))
            error = 0
            for i in list(range(self.var_range[0], self.var_range[1] + 1)):
                environment[variable] = i
                cal = int(abs((function(environment)) - node.eval(environment)))
                if cal == 0:
                    error = 0
                    break
                error -= abs((function(environment)) - node.eval(environment))
            error = error / len(list(range(self.var_range[0], self.var_range[1] + 1)))
            # score = - abs(node.eval(environment) - self.expected_number)
            return error

        super().__init__(function_F_AST_fitness)
