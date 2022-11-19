import math
from typing import List

from Chromosome import Chromosome
from functions.goldstein_price import goldstein_price
from selection import SelectionStrategy
from utils.sort_population import sort_population
from crorrsing import Crossing
from Mutation import Mutation
from inversion import Inversion


class Population:
    _chromosomes: List[Chromosome] = []
    _size: int = 0

    def __init__(self, size, selection: SelectionStrategy):
        self.__chromosomes_length = 0
        self._selection = selection
        self._size = size

    def generate(self, left_limit, right_limit):
        self.__chromosomes_length = Chromosome.calc_length(left_limit, right_limit)
        self._chromosomes = [Chromosome(
            left_limit,
            right_limit,
            self.__chromosomes_length,
            goldstein_price,
            []
        ) for _ in range(self._size)]

    def __elite_strategy(self, size):
        """
        Attributes:
            size: percentage size of population to maintain
        """
        # calculate how many members should be kept
        amount = math.ceil(len(self._chromosomes) * size)

        # sort array and get the best
        sorted_members = sort_population(self._chromosomes)
        saved = sorted_members[-amount:len(sorted_members)]
        # TODO min vs max
        # here is max
        operational = sorted_members[:-amount]

        return amount, saved, operational

    def get_best_value(self):
        sorted_population = sort_population(self._chromosomes)
        print(sorted_population[-1].value)

    def evolve(self, fitness):

        for _ in range(100):
            # strategy
            elite_members_amount, saved_elite_chromosomes, operational_chromosomes = self.__elite_strategy(0.2)

            # selection
            selected = self._selection.select(operational_chromosomes)

            # crossingn
            # to select the type of crossover type in (1,2,3)"crossed.call_crossover_functions(3)"

            # TODO change to selected once selections will be fixed
            crossed = Crossing(operational_chromosomes, 0.5, self._size, elite_members_amount)
            crossed.call_crossover_functions(1)

            # crossed.member_after_crossing_one_point - after crossing
            member_after_crossing = crossed.member_after_crossing_one_point

            # mutation
            mutated = Mutation(member_after_crossing, 0.1)

            # mutated.homogeneous_mutation()
            # mutated.edge_mutation()

            mutated.two_point_mutation()

            # print(mutated.member_after_mutation)

            # inversion
            # TODO probability from param
            population_inversion = Inversion(0.3)
            population_inversion.inversion_in_population(mutated.member_after_mutation)

            # print(population_inversion.inverted_population)

            # assign to _chromosomes
            # population_inversion.inverted_population
            self._chromosomes = [Chromosome(-2, 2, self.__chromosomes_length, fitness, initial_binary_gens)
                                 for initial_binary_gens in population_inversion.inverted_population] \
                                + saved_elite_chromosomes

            self.get_best_value()

            # dana iteracja wynik
