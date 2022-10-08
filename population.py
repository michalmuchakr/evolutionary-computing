import random
import numpy as np
from chromosome import Chromosome


class Population:
    # population

    def __init__(self, population_size):
        self.__members = []
        self.__population_size = population_size

    def generate_random_population(
            self,
            search_result_range_from,
            search_result_range_to,
            chromosome_gens_precision,
            fittness_function_precision
    ):
        # set precision for gens in chromosome
        np.set_printoptions(precision=4, suppress=True)

        for member in range(self.__population_size):
            # generate chromosome with two gens
            generated_initial_gens = np.random.uniform(
                low=search_result_range_from,
                high=search_result_range_to,
                size=2
            )
            generated_chromosome = Chromosome(generated_initial_gens, fittness_function_precision)

            self.__members.append(generated_chromosome)

    def print_population(self):
        for member in self.__members:
            print(member)

    def __str__(self):
        return "Population size: " + self.__population_size
