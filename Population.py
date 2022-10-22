import math

from Chromosome import Chromosome
from fitness_function import fitness_function

class Population:
    members = []
    selected_from_population = []

    def __init__(self, population_size):
        self.population_size = population_size

    def __len__(self):
        return self.population_size

    def __str__(self):
        return "Population size: " + self.population_size

    def set_selected_from_population(self, selected_from_population):
        self.selected_from_population = selected_from_population

    def get_members(self):
        return self.members

    def generate_random_population(
        self,
        search_result_range_from,
        search_result_range_to,
    ):
        chromosome_len = Chromosome.get_chromosome_len(search_result_range_from, search_result_range_to)

        for member in range(self.population_size):
            generated_chromosome = Chromosome(
                search_result_range_from, search_result_range_to, chromosome_len, fitness_function)

            self.members.append(generated_chromosome)

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
        amount = math.ceil(len(self.members) * size)
        # sort array and get the best
        sorted_members = sorted(self.members)
        selected_members = sorted_members[-amount:len(sorted_members)]
        return amount, selected_members

    def evolve(self):
        # strategy
        amount, maintained_members = self.__elite_strategy(0.3)

        # selection

        # crossing

        # mutation

        #inversion
