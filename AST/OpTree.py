from Node import Node


class OpTree(Node):
    def __init__(self, operation, left, right):
        self.operation = operation
        self.left = left
        self.right = right

    def eval(self, environment):
        return self.operation(self.left.eval(environment), self.right.eval(environment))

    def __str__(self):
        return f"({self.left} {self.operation} {self.right})"

