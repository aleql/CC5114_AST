
class Node:

    def eval(self, environment):
        raise NotImplemented()

    def mutate(self, operations, terminals, mutation_rate, rand):
        raise NotImplemented()

    def toList(self):
        raise NotImplemented

    def height(self):
        raise NotImplemented

    def copy(self):
        raise NotImplemented

    def __str__(self):
        raise NotImplemented()


