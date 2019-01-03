import random

from AST.OpTree import OpTree
from AST.ValTree import ValTree
from AST.VarTree import VarTree
from Operations.Add import Add
from Operations.Mul import Mul
from Operations.Sub import Sub


class TreeGenerator(object):

    def __init__(self, terminals, height, rand=random.Random(9001)):
        self.terminals = terminals
        self.height = height
        self.rand = rand
        self.operations = [Add(), Sub(), Mul()]

    # Inicial height= altura arbol, node = raiz
    def generate_tree(self, height):
        # Base case
        if height == 1:
            terminal = random.choice(self.terminals)

            # Variable
            if isinstance(terminal, str):
                return VarTree(terminal)
            # Value
            else:
                return ValTree(terminal)

        # Recursive case
        else:

            # Operator
            if self.rand.random() > 0.5:
                operator = random.choice(self.operations)
                return OpTree(operator, self.generate_tree(height - 1), self.generate_tree(height - 1))

            # Variable of value
            terminal = random.choice(self.terminals)

            # Variable
            if isinstance(terminal, str):
                return VarTree(terminal)

            # Value
            else:
                return ValTree(terminal)

    def mutate_tree(self, node, mutation_rate):
        return node.mutate(self.operations, self.terminals, mutation_rate, self.rand)



