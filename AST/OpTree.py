from AST.Node import Node


class OpTree(Node):
    def __init__(self, operation, left, right):
        self.operation = operation
        self.left = left
        self.right = right

    def eval(self, environment):
        eval_izq = self.left.eval(environment)
        eval_der = self.right.eval(environment)
        return self.operation.operate(eval_izq, eval_der)

    def __str__(self):
        return f"({self.left} {self.operation} {self.right})"

    def toList(self):
        return [self, self.left, self.right]

    def mutate(self, operations, terminals, mutation_rate, rand):

        # Mutate this node
        if mutation_rate > rand.random():

            # Ensure is a new operation
            mutated_operation = rand.choice(operations)
            while mutated_operation == self.operation:
                mutated_operation = rand.choice(operations)
            self.operation = mutated_operation

        # Recursive call
        self.left = self.left.mutate(operations, terminals, mutation_rate, rand)
        self.right = self.right.mutate(operations, terminals, mutation_rate, rand)

        return self

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def copy(self):
        left_copy = self.left.copy()
        right_copy = self.right.copy()

        return OpTree(self.operation, left_copy, right_copy)

