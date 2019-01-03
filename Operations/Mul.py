from Operations.Operation import Operation


class Mul(Operation):

    def operate(self, x, y):
        return x * y

    def __str__(self):
        return "*"
