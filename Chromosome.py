import math
import random

from utils.binary_to_decimal import binary_to_decimal

class Chromosome:
    _binary_gens = [] # binary gens for X1, X2 [[bool], [bool]]
    dec_gens = [] # decimal gens for X1, X2 [float, float]
    value = 0

    def __init__(self, left_limit, right_limit, lenght, fitness):
        """
        Attributes:
            lefy_limit: lower limit of the final value
            right_limit: upper limit of the final value
            lenght: lenght of the chromosome
            fitness: fitness function
        """
        self._binary_gens = self.__generate(lenght)
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.dec_gens = self.__bin_to_decimal()
        self.value = fitness(self.dec_gens[0], self.dec_gens[1])

    @property
    def binary_gens(self):
        return self._binary_gens

    @binary_gens.setter
    def binary_gens(self, new_binary_gens):
        self._binary_gens = new_binary_gens

    def __generate(self, chromosome_len):
        gen = [bool(random.randint(0, 1)) for _ in range(chromosome_len)]
        return [gen, gen]

    def __bin_to_decimal(self):
        return [binary_to_decimal(self.binary_gens[index], self.left_limit, self.right_limit) for index in range(2)]

    @staticmethod
    def calc_length(search_result_range_from, search_result_range_to):
        return int(math.log2((search_result_range_to - search_result_range_from) * pow(10, 6)))
