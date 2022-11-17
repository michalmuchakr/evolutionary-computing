import math
from typing import List

from Chromosome import Chromosome
from functions.goldstein_price import goldstein_price
from selection import SelectionStrategy
from utils.sort_population import sort_population
from Crossing import Crossing
from Mutation import Mutation


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

        amount, saved_chromosomes, operational_chromosomes = self.__elite_strategy(0.2)

        # selection
        selected = self._selection.select(operational_chromosomes)

        # crossingn
        #to select the type of crossover type in (1,2,3)"crossed.call_crossover_functions(3)"
        crossed = Crossing(operational_chromosomes,0.5,self._size)
        crossed.call_crossover_functions(1)
        member_after_crossing = crossed.member_after_crossing_one_point

        # mutation
        mutated = Mutation(member_after_crossing,0.1)
        #mutated.homogeneous_mutation()
        #mutated.edge_mutation()
        mutated.two_point_mutation()
        print(mutated.member_after_mutation)

        # inversion

        # assign to _chromosomes

        # TODO: remove after developing
        print(selected)

        #dana iteracja wynik


