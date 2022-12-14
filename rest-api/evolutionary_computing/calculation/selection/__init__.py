from abc import ABC, abstractmethod
import math
from random import random

from evolutionary_computing.calculation.utils.split_into_chunks import split_list_into_chunks
from evolutionary_computing.calculation.utils.sort_population import sort_population


class SelectionStrategy(ABC):
    @abstractmethod
    def select(self, members, to_be_selected_amount, problem_to_solve):
        pass


class RouletteSelection(SelectionStrategy):
    members_roulette_probability_distributor = []

    def __init__(self):
        self.members_roulette_probability_distributor = []

    def get_index_element_by_distributor(self, draw_distributor):
        for draw_result_item_index, probability_distributor in enumerate(self.members_roulette_probability_distributor):
            if probability_distributor[1] > draw_distributor:
                return draw_result_item_index

    def select(self, members, to_be_selected_amount, problem_to_solve):
        self.members_roulette_probability_distributor = []
        population_to_select_from_members = members

        # calc fin fun sum for all members
        all_members_fit_fun_sum = 0
        for member in population_to_select_from_members:
            if problem_to_solve == 'minimization':
                all_members_fit_fun_sum += 1 / member.value
            else:
                all_members_fit_fun_sum += member.value

        # Calc probability and distributor for each population member
        # members_roulette_probability_distributor = [[probability, distributor]]
        for index, member in enumerate(population_to_select_from_members):
            member_probability_distributor = []

            # probability
            if problem_to_solve == 'minimization':
                member_probability = (1 / member.value) / all_members_fit_fun_sum
            else:
                member_probability = member.value / all_members_fit_fun_sum

            member_probability_distributor.append(member_probability)

            # distributor
            if index == 0:
                member_probability_distributor.append(member_probability)
            else:
                member_distributor = self.members_roulette_probability_distributor[index - 1][1] + member_probability
                member_probability_distributor.append(member_distributor)

            self.members_roulette_probability_distributor.append(member_probability_distributor)

        return [members[self.get_index_element_by_distributor(random())] for _ in range(to_be_selected_amount)]


class TournamentSelection(SelectionStrategy):

    def select(self, members, to_be_selected_amount, problem_to_solve):
        chunked_population_for_tournament = split_list_into_chunks(members, to_be_selected_amount)

        # sort chunks by fit function
        for index, tournament_chunk in enumerate(chunked_population_for_tournament):
            chunked_population_for_tournament[index] = sort_population(
                tournament_chunk
            )

        # select best in each chunk
        for index, tournament_chunk in enumerate(chunked_population_for_tournament):
            chunked_population_for_tournament[index] = chunked_population_for_tournament[index][0]

        return chunked_population_for_tournament


class BestFitSelection(SelectionStrategy):
    def select(self, members, to_be_selected_amount, problem_to_solve):
        population_to_select_from_members = members
        sorted_population = sort_population(population_to_select_from_members)

        # get the best members from stack
        return sorted_population[0:to_be_selected_amount]
