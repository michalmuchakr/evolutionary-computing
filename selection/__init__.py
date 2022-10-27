from abc import ABC, abstractmethod
import math

from utils.split_into_chunks import split_list_into_chunks
from utils.sort_population import sort_population


class SelectionStrategy(ABC):
    @abstractmethod
    def select(self, members):
        pass


class RouletteSelection(SelectionStrategy):
    def select(self, members):
        population_to_select_from_members = members

        # calc fin fun sum for all members
        all_members_fit_fun_sum = 0
        for member in population_to_select_from_members:
            all_members_fit_fun_sum += 1 / member.value

        # Calc probability and distributor for each population member
        # members_roulette_probability_distributor = [[probability, distributor]]
        members_roulette_probability_distributor = []

        for index, member in enumerate(population_to_select_from_members):
            member_probability_distributor = []

            # probability
            member_probability = (1 / member.value) / all_members_fit_fun_sum
            member_probability_distributor.append(member_probability)

            # distributor
            if index == 0:
                member_probability_distributor.append(member_probability)
            else:
                member_distributor = members_roulette_probability_distributor[index - 1][1] + member_probability
                member_probability_distributor.append(member_distributor)

            members_roulette_probability_distributor.append(member_probability_distributor)

        return members_roulette_probability_distributor


class TournamentSelection(SelectionStrategy):
    def __init__(self, group_size):
        self._group_size = group_size

    def select(self, members):
        chunked_population_for_tournament = split_list_into_chunks(members, self._group_size)

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
    def __init__(self, percentage_selection, population_size):
        self._percentage_selection = percentage_selection
        self._population_size = population_size

    def select(self, members):
        population_to_select_from_members = members
        sorted_population = sort_population(population_to_select_from_members)
        last_best_member_index = math.floor(self._population_size * self._percentage_selection / 100)

        # get the best members from stack
        return sorted_population[0:last_best_member_index]
