from functools import reduce

from Calculator.Fitness_Calculator import Fitness_Calculator


class Seq_Calculator(Fitness_Calculator):

    def __init__(self, expected_sequence):

        def exp_seq_fitness(chromosome):
            diff_list = map((lambda x: 1 if x[0] == x[1] else 0), list(zip(chromosome, expected_sequence)))
            score = reduce((lambda x, y: x + y), diff_list)
            return score

        super().__init__(exp_seq_fitness)

'''
mutacion recursiva, solo cambia entre terminales y operacioenes, mantiene el resto bien

mating: todas las combinaciones [a, a.izq, a.der], [b, b.der, b.izq], [op]

'''