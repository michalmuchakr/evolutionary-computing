import math
from typing import List

from Chromosome import Chromosome
from functions.goldstein_price import goldstein_price
from selection import SelectionStrategy
from utils.sort_population import sort_population

class Population:
    _chromosome: List[Chromosome] = []
    _size: int = 0

    def __init__(self, size, selection: SelectionStrategy):
        self._selection = selection
        self._size = size

    def generate(self, left_limit, right_limit):
        chromosome_len = Chromosome.calc_length(left_limit, right_limit)
        self.all_members = [Chromosome(left_limit, right_limit, chromosome_len, goldstein_price) for _ in range(self._size)]

    def __elite_strategy(self, size):
        """
        Attributes:
            size: percentage size of population to maintain
        """
        # calculate how many mebers should be kept
        amount = math.ceil(len(self.all_members) * size)
        # sort array and get the best
        sorted_members = sort_population(self.all_members)
        saved = sorted_members[-amount:len(sorted_members)]
        operational = sorted_members[:-amount]

        return amount, saved, operational

    def evolve(self):
        # strategy
        amount, savet_chromosomes, operational_chromosomes = self.__elite_strategy(0.3)

        # selection
        selected = self._selection.select(self.all_members)

        # crossing

        # mutation

        #inversion

        print(selected)
