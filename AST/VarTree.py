from AST.Node import Node


class VarTree(Node):

    def __init__(self, variable, left=None, right=None):
        self.variable = variable
        self.left = left
        self.right = right

    def eval(self, environment):
        eval = environment[self.variable]
        return eval

    def __str__(self):
        return f"{self.variable}"

    def toList(self):
        return [self]

    def mutate(self, operations, terminals, mutation_rate, rand):
        # Mutate this node
        if mutation_rate > rand.random():

            # Ensure mutation is a new variable
            mutated_variable = rand.choice(terminals)
            while mutated_variable == self.variable or isinstance(mutated_variable, int):
                mutated_variable = rand.choice(terminals)

            self.variable = mutated_variable

        return self

    def height(self):
        return 1

    def copy(self):
        return VarTree(self.variable)
