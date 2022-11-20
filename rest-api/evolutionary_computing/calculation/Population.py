import math
from typing import List

from evolutionary_computing.calculation.Chromosome import Chromosome
from evolutionary_computing.calculation.functions.goldstein_price import goldstein_price
from evolutionary_computing.calculation.selection import SelectionStrategy
from evolutionary_computing.calculation.utils.sort_population import sort_population
# from .crorrsing import Crossing
from evolutionary_computing.calculation.Mutation import Mutation
from evolutionary_computing.calculation.inversion import Inversion


class Population:
    _calculation_results = []
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

    def __elite_strategy(self, elite_percentage):
        """
        Attributes:
            elite_percentage: percentage size of population to maintain
        """
        # calculate how many members should be kept
        amount = math.ceil(len(self._chromosomes) * elite_percentage)

        # sort array and get the best
        sorted_members = sort_population(self._chromosomes)
        saved = sorted_members[-amount:len(sorted_members)]

        # TODO min vs max
        # here is max
        operational = sorted_members[:-amount]

        return amount, saved, operational

    def get_best_value(self, epoch_index):
        sorted_population = sort_population(self._chromosomes)
        return epoch_index + 1, \
               sorted_population[-1].dec_gens[0], \
               sorted_population[-1].dec_gens[1], \
               sorted_population[-1].value

    def evolve(self, fitness, crossing, epoch_amount, elite_percentage):
        for epoch_index in range(epoch_amount):
            # 1. strategy
            elite_members_amount, saved_elite_chromosomes, operational_chromosomes = \
                self.__elite_strategy(elite_percentage / 100)

            to_be_selected_amount = math.ceil((self._size * ((100 - elite_percentage) / 100)) / 2)

            # 2. selection
            # TODO all population members
            selected = self._selection.select(operational_chromosomes, to_be_selected_amount)

            # 3. crossing
            # to select the type of crossover type in (1,2,3)"crossed.call_crossover_functions(3)"

            member_after_crossing = crossing.cross(selected, 0.5)

            # crossed = Crossing(selected, 0.8, self._size, elite_members_amount)
            # crossed.call_crossover_functions(3)

            # crossed.member_after_crossing_one_point - after crossing
            # member_after_crossing = crossed.member_after_crossing_one_point

            # mutation
            mutated = Mutation(member_after_crossing, 0.8)

            # mutated.homogeneous_mutation()
            # mutated.edge_mutation()

            mutated.two_point_mutation()

            # print(mutated.member_after_mutation)

            # inversion
            # TODO probability from param
            population_inversion = Inversion(0.8)
            inverted_population = population_inversion.inversion_in_population(mutated.member_after_mutation)

            # print(population_inversion.inverted_population)

            # assign to _chromosomes
            # population_inversion.inverted_population
            self._chromosomes = []
            self._chromosomes = [Chromosome(-2, 2, self.__chromosomes_length, fitness, initial_binary_gens)
                                 for initial_binary_gens in inverted_population] \
                                + saved_elite_chromosomes

            # X1, X2, FitFun(x1, x2), srednie odchylenie standardowe dla całej populacji
            # -> baza danych

            self._calculation_results.append(self.get_best_value(epoch_index))

        return self._calculation_results
