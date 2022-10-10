import numpy

from chromosome import Chromosome


class Population:
    # population

    def __init__(self, population_size):
        self.__members = []
        self.__selected_from_population = []
        self.__population_size = population_size

    def len(self):
        return self.__population_size

    def set_selected_from_population(self, selected_from_population):
        self.__selected_from_population = selected_from_population

    def get_members(self):
        return self.__members

    def generate_random_population(
        self,
        search_result_range_from,
        search_result_range_to,
        chromosome_gens_precision,
        fittness_function_precision
    ):
        # set precision for gens in chromosome
        numpy.set_printoptions(precision=chromosome_gens_precision, suppress=True)

        for member in range(self.__population_size):
            # generate chromosome with two gens
            generated_initial_gens = numpy.random.uniform(
                low=search_result_range_from,
                high=search_result_range_to,
                size=2
            )
            generated_chromosome = Chromosome(generated_initial_gens, fittness_function_precision)

            self.__members.append(generated_chromosome)

    def print_population(self):
        for member in self.__members:
            print(member)

    def print_selected_from_population(self):
        for member in self.__selected_from_population:
            print(member)

    def __str__(self):
        return "Population size: " + self.__population_size
