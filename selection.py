import math

from utility import split_list_into_chunks


class Selection:
    # Selection algorithms

    @staticmethod
    def tournament_members_selection(population_to_select_members, tournament_selection_groups_size):
        chunked_population_for_tournament = split_list_into_chunks(population_to_select_members.get_members(),
                                                                   tournament_selection_groups_size)

        # sort chunks by fit function
        for index, tournament_chunk in enumerate(chunked_population_for_tournament):
            chunked_population_for_tournament[index] = Selection.sort_members_by_fit_function(
                tournament_chunk
            )

        # select best in each chunk
        for index, tournament_chunk in enumerate(chunked_population_for_tournament):
            chunked_population_for_tournament[index] = chunked_population_for_tournament[index][0]

        return chunked_population_for_tournament

    @staticmethod
    def get_best_members_by_fit_function_by_percentage(
        population_to_select_from,
        best_members_selection_percentage,
        population_size
    ):
        population_to_select_from_members = population_to_select_from.get_members()
        sorted_population = Selection.sort_members_by_fit_function(population_to_select_from_members)
        last_best_member_index = math.floor(population_size * best_members_selection_percentage / 100)

        return sorted_population[0:last_best_member_index]

    @staticmethod
    def sort_members_by_fit_function(population_to_be_sorted):
        # sort population members in ascending order
        sorted_population = sorted(
            population_to_be_sorted,
            key=lambda member: member.get_fitness_function_val()
        )
        return sorted_population
