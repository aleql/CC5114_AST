from AST.Node import Node


class ValTree(Node):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def eval(self, environment):
        return self.value

    def __str__(self):
        return f"{self.value}"

    def toList(self):
        return [self]

    def mutate(self, operations, terminals, mutation_rate, rand):
        # Mutate this node
        if mutation_rate > rand.random():

            # Ensure mutation is a new value
            mutated_value = rand.choice(terminals)
            while mutated_value == self.value or isinstance(mutated_value, str):
                mutated_value = rand.choice(terminals)

            self.value = mutated_value

        # check
        if isinstance(self.value, str):
            raise Exception("ERROR VAL {}".format(self.value))

        return self

    def height(self):
        return 1

    def copy(self):
        return ValTree(self.value)

