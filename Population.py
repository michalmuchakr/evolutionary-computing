import math
from typing import List

from Chromosome import Chromosome
from functions.goldstein_price import goldstein_price
from selection import SelectionStrategy
from utils.sort_population import sort_population


class Population:
    _chromosomes: List[Chromosome] = []
    _size: int = 0

    def __init__(self, size, selection: SelectionStrategy):
        self._selection = selection
        self._size = size

    def generate(self, left_limit, right_limit):
        chromosome_len = Chromosome.calc_length(left_limit, right_limit)
        self._chromosomes = [Chromosome(left_limit, right_limit, chromosome_len, goldstein_price) for _ in
                             range(self._size)]

    def __elite_strategy(self, size):
        """
        Attributes:
            size: percentage size of population to maintain
        """
        # calculate how many mebers should be kept
        amount = math.ceil(len(self._chromosomes) * size)
        # sort array and get the best
        sorted_members = sort_population(self._chromosomes)
        saved = sorted_members[-amount:len(sorted_members)]
        operational = sorted_members[:-amount]

        return amount, saved, operational

    def evolve(self):
        # strategy
        amount, saved_chromosomes, operational_chromosomes = self.__elite_strategy(0.1)

        # selection
        selected = self._selection.select(operational_chromosomes)

        # crossing

        # mutation

        # inversion

        # assign to _chromosomes

        # TODO: remove after developing
        print(selected)
