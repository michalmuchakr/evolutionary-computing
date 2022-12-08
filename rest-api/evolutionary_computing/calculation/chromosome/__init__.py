import math
import random

from evolutionary_computing.calculation.utils.binary_to_decimal import binary_to_decimal


class Chromosome:
    _binary_gens = []  # binary gens for X1, X2 [[bool], [bool]]
    dec_gens = []  # decimal gens for X1, X2 [float, float]
    value = 0

    def __init__(self, left_limit, right_limit, length, fitness, initial_gens, gene_type):
        """
        Attributes:
            left_limit: lower limit of the final value
            right_limit: upper limit of the final value
            length: length of the chromosome
            fitness: fitness function
            initial_gens: [bool[], bool[]]
        """
        if gene_type == 'binary' or len(initial_gens) == 0:
            self._binary_gens = self.__generate(length, initial_gens)

        self.left_limit = left_limit
        self.right_limit = right_limit

        if gene_type == 'binary' or len(initial_gens) == 0:
            self.dec_gens = self.__bin_to_decimal()
        else:
            self.dec_gens = initial_gens

        self.value = fitness(self.dec_gens[0], self.dec_gens[1])

    @property
    def binary_gens(self):
        return self._binary_gens

    @binary_gens.setter
    def binary_gens(self, new_binary_gens):
        self._binary_gens = new_binary_gens

    @staticmethod
    def __generate(chromosome_len, initial_binary_gens):
        if len(initial_binary_gens) > 0:
            return initial_binary_gens
        else:
            return [
                [bool(random.randint(0, 1)) for _ in range(chromosome_len)]
                for _ in range(2)
            ]

    def __bin_to_decimal(self):
        return [binary_to_decimal(self.binary_gens[index], self.left_limit, self.right_limit) for index in range(2)]

    @staticmethod
    def calc_length(search_result_range_from, search_result_range_to):
        return int(math.log2((search_result_range_to - search_result_range_from) * pow(10, 6)))
