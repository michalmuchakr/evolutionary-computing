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
        self.binary_gens = self.init_gens(lenght)
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.dec_gens = self.get_dec_gen_from_binary()
        self.value = fitness(self.dec_gens[0],self.dec_gens[1])

    def __str__(self):
        return "(" + str(self.binary_gens[0]) + ", " + str(self.binary_gens[1]) + ") = " + str(self.value)

    @property
    def binary_gens(self):
        return self._binary_gens

    @binary_gens.setter
    def binary_gens(self, new_binary_gens):
        self._binary_gens = new_binary_gens

    def init_gens(self, chromosome_len):
        gen = [bool(random.randint(0, 1)) for _ in range(chromosome_len)]
        return [gen, gen]

    def get_dec_gen_from_binary(self):
        return [binary_to_decimal(self.binary_gens[index], self.left_limit, self.right_limit) for index in range(2)]

    @staticmethod
    def get_chromosome_len(search_result_range_from, search_result_range_to):
        return int(math.log2((search_result_range_to - search_result_range_from) * pow(10, 6)))
