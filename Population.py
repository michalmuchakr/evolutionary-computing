import math
from typing import List

from Chromosome import Chromosome
from functions.goldstein_price import goldstein_price
from selection import SelectionStrategy
from utils.sort_population import sort_population

class Population:
    all_members: List[Chromosome] = []
    selected_from_population = []
    saved_members = []
    operational_members = []
    population_size = 0

    def __init__(self, population_size, selection: SelectionStrategy):
        self.population_size = population_size
        self._selection = selection

    def __len__(self):
        return self.population_size

    def __str__(self):
        return "Population size: " + self.population_size

    def set_selected_from_population(self, selected_from_population):
        self.selected_from_population = selected_from_population

    def get_members(self):
        return self.all_members

    def generate_random_population(
        self,
        search_result_range_from,
        search_result_range_to,
    ):
        chromosome_len = Chromosome.calc_length(search_result_range_from, search_result_range_to)

        for member in range(self.population_size):
            generated_chromosome = Chromosome(
                search_result_range_from, search_result_range_to, chromosome_len, goldstein_price)

            self.all_members.append(generated_chromosome)

    def print_population(self):
        for member in self.members:
            print(member)

    def print_selected_from_population(self):
        for member in self.selected_from_population:
            print(member)

    def __elite_strategy(self, size):
        """
        Attributes:
            size: percentage size of population to maintain
        """
        # calculate how many mebers should be kept
        amount = math.ceil(len(self.all_members) * size)
        # sort array and get the best
        sorted_members = sort_population(self.all_members)
        self.saved_members = sorted_members[-amount:len(sorted_members)]
        self.operational_members = sorted_members[:-amount]

        return amount, self.saved_members, self.operational_members

    def evolve(self):
        # strategy
        self.__elite_strategy(0.3)

        # selection
        selected = self._selection.select(self.all_members)

        # crossing

        # mutation

        #inversion

        print(selected)
