from Operations.Operation import Operation


class Add(Operation):

    def operate(self, x, y):
        # print("sum", x, y)
        return x + y

    def __str__(self):
        return "+"
