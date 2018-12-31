from Node import Node


class ValTree(Node):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def eval(self, environment):
        return self.value

    def __str__(self):
        return f"{self.value}"
