import unittest

from Generator.Generator import Generator

class Test_generator(unittest.TestCase):

    def test_binary_genes(self):
        pool = ["0", "1"]
        length = 5
        self.generator = Generator(pool, length)

        # Generate a sequence
        assert self.generator.generate_sequence() == "01101", "Failed test test_binary_genes, generated wrong sequence"

        # Generate a single gen
        assert self.generator.generate_single_gen() == "0", "Failed test test_binary_genes, generated wrong single gen"

    def test_char_genes(self):
        pool = list("abcdefghijklmnñopqrstuvwxyz")
        length = 5
        self.generator = Generator(pool, length)

        # Generate a sequence
        assert self.generator.generate_sequence() == "bjicr", "Failed test test_char_genes, generated wrong sequence"

        # Generate a single gen
        assert self.generator.generate_single_gen() == "i", "Failed test test_char_genes, generated wrong single gen"


