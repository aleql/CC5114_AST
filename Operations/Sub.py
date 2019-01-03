from Operations.Operation import Operation


class Sub(Operation):

    def operate(self, x, y):
        return x - y

    def __str__(self):
        return "-"
