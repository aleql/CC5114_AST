from Node import Node


class VarTree(Node):

    def __init__(self, variable, left=None, right=None):
        self.variable = variable
        self.left = left
        self.right = right

    def eval(self, environment):
        return environment[self.variable]

    def __str__(self):
        return f"{self.variable}"
