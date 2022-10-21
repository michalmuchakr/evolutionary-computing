import math
import random

from fitness_function import fitness_function


class Chromosome:
    # chromosome

    # binary gens for X1, X2 ['string', 'string']
    binary_gens = []

    # binary gens for X1, X2 ['float', 'float']
    dec_gens = []

    def __init__(self, search_result_range_from, search_result_range_to, chromosome_len):
        self.binary_gens = self.get_initial_gens(chromosome_len)
        self.dec_gens = self.get_dec_gen_from_binary(search_result_range_from, search_result_range_to, chromosome_len)

        self.fitness_function_val = fitness_function(
            self.dec_gens[0],
            self.dec_gens[1]
        )

    def binary_to_decimal(self, a, search_result_range_to):
        pass

    def get_fitness_function_val(self):
        return self.fitness_function_val

    def str(self):
        return "(" + str(self.binary_gens[0]) + ", " + str(self.binary_gens[1]) + ") = " + \
                str(self.fitness_function_val)

    @staticmethod
    def generate_chromosome_bin(chromosome_len):
        return ''.join([str(random.randint(0, 1)) for _ in range(chromosome_len)])

    @staticmethod
    def get_chromosome_len(search_result_range_from, search_result_range_to):
        return int(math.log2((search_result_range_to - search_result_range_from) * pow(10, 6)))

    @staticmethod
    def decode_binary_value_to_decimal(binary_to_decode,
                                        search_result_range_from,
                                        search_result_range_to,
                                        chromosome_len):
        return search_result_range_from + int(binary_to_decode, 2) * (
            search_result_range_to - search_result_range_from) / (pow(2, chromosome_len) - 1)

    def get_initial_gens(self, chromosome_len):
        initial_gen = self.generate_chromosome_bin(chromosome_len)
        return [initial_gen, initial_gen]

    def get_dec_gen_from_binary(self, search_result_range_from, search_result_range_to, chromosome_len):
        return [self.decode_binary_value_to_decimal(self.binary_gens[index],
                                                    search_result_range_from,
                                                    search_result_range_to,
                                                    chromosome_len
                                                    ) for index in range(2)]
