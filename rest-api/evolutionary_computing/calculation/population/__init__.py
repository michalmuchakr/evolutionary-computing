import math
from typing import List

import numpy as np

from evolutionary_computing.calculation.chromosome import Chromosome
from evolutionary_computing.calculation.functions.goldstein_price import goldstein_price
from evolutionary_computing.calculation.selection import SelectionStrategy
from evolutionary_computing.calculation.utils.decimal_to_percentage import decimal_to_percentage
from evolutionary_computing.calculation.utils.sort_population import sort_population
from evolutionary_computing.calculation.inversion import Inversion


class Population:
    _calculation_results = []
    _chromosomes: List[Chromosome] = []
    _size: int = 0

    def __init__(self, size, selection: SelectionStrategy, gene_type):
        self.__chromosomes_length = 0
        self._selection = selection
        self._size = size
        self.gene_type = gene_type

    def generate(self, left_limit, right_limit):
        self.__chromosomes_length = Chromosome.calc_length(left_limit, right_limit)
        self._chromosomes = [Chromosome(
            left_limit,
            right_limit,
            self.__chromosomes_length,
            goldstein_price,
            [],
            self.gene_type
        ) for _ in range(self._size)]

    def __elite_strategy(self, elite_percentage, problem_to_solve):
        """
        Attributes:
            elite_percentage: percentage size of population to maintain
        """
        # calculate how many members should be kept
        amount = math.ceil(len(self._chromosomes) * decimal_to_percentage(elite_percentage))

        # sort array and get the best
        sorted_members = sort_population(self._chromosomes)

        if problem_to_solve == 'maximization':
            operational = sorted_members[:-amount]
            saved = sorted_members[-amount:len(sorted_members)]
        else:
            operational = sorted_members[amount:]
            saved = sorted_members[:amount]

        return amount, saved, operational

    def calc_variation(self, epoch_res_chromosomes):
        pass

    def get_formatted_result(self, epoch_index, problem_to_solve):
        sorted_population = sort_population(self._chromosomes)

        variation = np.var([chromosome.value for chromosome in self._chromosomes])

        if problem_to_solve == 'maximization':
            return epoch_index + 1, \
                   sorted_population[-1].dec_gens[0], \
                   sorted_population[-1].dec_gens[1], \
                   sorted_population[-1].value, \
                   variation
        else:
            return epoch_index + 1, \
                   sorted_population[0].dec_gens[0], \
                   sorted_population[0].dec_gens[1], \
                   sorted_population[0].value, \
                   variation

    def evolve(
        self,
        gene_type,
        fitness,
        crossing,
        epoch_amount,
        elite_percentage,
        problem_to_solve,
        probability_of_mutation,
        probability_of_crossing,
        probability_of_inversion,
        search_result_range_from,
        search_result_range_to,
        mutation
    ):
        """
            1. strategy
            2. selection
            3. crossing
            4. mutation
            5. inversion
            6. reassign population with calculated members
            7. result aggregation
        """
        self._calculation_results = []

        for epoch_index in range(epoch_amount):
            # 1. strategy
            elite_members_amount, saved_elite_chromosomes, operational_chromosomes = \
                self.__elite_strategy(elite_percentage, problem_to_solve)

            to_be_selected_amount = math.ceil((self._size - elite_members_amount) / 2)

            # 2. selection
            selected = self._selection.select(
                operational_chromosomes,
                to_be_selected_amount,
                problem_to_solve
            )

            # 3. crossing
            member_after_crossing = crossing.cross(selected, probability_of_crossing, problem_to_solve)

            # 4. mutation
            member_after_mutation = mutation.mutate(member_after_crossing,
                                                    probability_of_mutation,
                                                    search_result_range_from,
                                                    search_result_range_to)

            # 5. inversion
            if gene_type == 'binary':
                population_inversion = Inversion(probability_of_inversion)
                member_after_mutation = population_inversion.inversion_in_population(member_after_mutation)

            # 6. assign to _chromosomes
            self._chromosomes = []
            self._chromosomes = \
                [Chromosome(
                    search_result_range_from,
                    search_result_range_to,
                    self.__chromosomes_length,
                    fitness,
                    initial_gens,
                    gene_type
                ) for initial_gens in member_after_mutation] \
                + saved_elite_chromosomes

            # 7. result aggregation
            self._calculation_results.append(self.get_formatted_result(epoch_index, problem_to_solve))

        return self._calculation_results
