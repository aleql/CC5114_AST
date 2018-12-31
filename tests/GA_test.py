import unittest

from Calculator.Seq_Calculator import Seq_Calculator
from Generator.Generator import Generator
from GA.GeneticAlgorithm import GeneticAlgorithm



class Test_generator(unittest.TestCase):

    def test_binary_genetic_algorithm(self):
        self.generator = Generator(['0', '1'], 5)
        self.calculator = Seq_Calculator("01010")
        self.GA = GeneticAlgorithm(self.generator, 8, self.calculator)
        self.GA.initialize_population()
        generations, chromosome = self.GA.genetic_algorithm()

        assert generations == 4, "GA did not converge on generation 4"
        assert chromosome == "01010", "GA did not converge to the right chromosome"

    def test_character_genetic_algorithm(self):
        self.generator = Generator(list("abcdefghijklmnñopqrstuvwxyz"), 10)
        self.calculator = Seq_Calculator("murcielago")
        self.GA = GeneticAlgorithm(self.generator, 16, self.calculator)
        self.GA.initialize_population()
        generations, chromosome = self.GA.genetic_algorithm()

        assert generations == 659, "GA did not converge on generation 4"
        assert chromosome == "murcielago", "GA did not converge to the right chromosome"





