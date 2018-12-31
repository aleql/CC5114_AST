import random
from operator import add, sub, mul

from OpTree import OpTree
from ValTree import ValTree
from VarTree import VarTree


class TreeGenerator(object):

    def __init__(self, terminals, height, rand=random.Random(9001)):
        self.terminals = terminals
        self.height = height
        self.rand = rand
        self.operators = [add, sub, mul]

    # Inicial height= altura arbol, node = raiz
    def generate_tree(self, height):
        # Base case
        if height == 1:
            terminal = random.choice(self.terminals)

            # Variable
            if type(terminal) == str:
                return VarTree(terminal)

            # Value
            else:
                return ValTree(terminal)

        # Recursive case
        else:

            # Operator
            if self.rand.random() > 0.5:
                print("OP")
                operator = random.choice(self.operators)
                return OpTree(operator, self.generate_tree(height - 1), self.generate_tree(height - 1))

            # Variable of value
            terminal = random.choice(self.terminals)

            # Variable
            if type(terminal) == str:
                return VarTree(terminal)

            # Value
            else:
                return ValTree(terminal)


