import random


class Generator:

    def __init__(self, pool, length, rand=random.Random(9001)):
        self.pool = pool
        self.length = length
        self.rand = rand

    def generate_single_gen(self):
        return self.rand.choice(self.pool)

    def generate_sequence(self):
        return "".join([self.generate_single_gen() for _ in range(self.length)])


