
class Fitness_Calculator:

    def __init__(self, fitness_function=None):
        self.fitness_function = fitness_function

    def calculate_fitness(self, chromosome):
        return (self.fitness_function(chromosome))
