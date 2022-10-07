import random
import numpy as np
from chromosome import Chromosome


class Population:
    # population

    def __init__(self, population_size):
        self.__members = []
        self.__population_size = population_size

    def generate_random_population(self, range_from, range_to):
        # set precision for gens in chromosome
        np.set_printoptions(precision=4, suppress=True)

        for member in range(self.__population_size):
            # generate chromosome with two gens
            initial_gens = np.random.uniform(low=range_from, high=range_to, size=2)
            generated_chromosome = Chromosome(initial_gens)

            self.__members.append(generated_chromosome)
