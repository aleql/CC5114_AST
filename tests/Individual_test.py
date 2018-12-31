import unittest

from Generator.Generator import Generator
from Individual.Individual import Individual


class Test_individual(unittest.TestCase):

    def test_binary_chromosome(self):
        pool = ["0", "1"]
        length = 5
        self.generator = Generator(pool, length)
        self.Individual = Individual(self.generator.generate_sequence())

        # Generate a sequence
        assert self.Individual.chromosome == "01101", "Failed test test_binary_chromosome, generated wrong sequence"

        # Test fitness
        assert self.Individual.evaluate_fitness("01101") == 5, "Failed test test_binary_chromosome, got wrong fitness " \
                                                               "instead of 5 "
        assert self.Individual.evaluate_fitness("11011") == 2, "Failed test test_binary_chromosome, got wrong fitness " \
                                                               "instead of 2 "

    def test_character_chromosome(self):
        pool = list("abcdefghijklmnñopqrstuvwxyz")
        length = 5
        self.generator = Generator(pool, length)
        self.Individual = Individual(self.generator.generate_sequence())

        # Generate a sequence
        assert self.Individual.chromosome == "bjicr", "Failed test test_binary_chromosome, generated wrong sequence"

        # Test fitness
        assert self.Individual.evaluate_fitness("bjicr") == 5, "Failed test test_binary_chromosome, got wrong fitness " \
                                                               "instead of 5 "
        assert self.Individual.evaluate_fitness("bjcri") == 2, "Failed test test_binary_chromosome, got wrong fitness " \
                                                               "instead of 2 "


