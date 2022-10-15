import math

from utility import split_list_into_chunks


class Selection:
    # Selection algorithms

    @staticmethod
    def roulette_wheel_members_selection(population_to_select_members):
        population_to_select_from_members = population_to_select_members.get_members()

        # calc fin fun sum for all members
        all_members_fit_fun_sum = 0
        for member in population_to_select_from_members:
            all_members_fit_fun_sum += 1 / member.get_fitness_function_val()

        # Calc probability and distributor for each population member
        # members_roulette_probability_distributor = [[probability, distributor]]
        members_roulette_probability_distributor = []

        for index, member in enumerate(population_to_select_from_members):
            member_probability_distributor = []

            # probability
            member_probability = (1 / member.get_fitness_function_val()) / all_members_fit_fun_sum
            member_probability_distributor.append(member_probability)

            # distributor
            if index == 0:
                member_probability_distributor.append(member_probability)
            else:
                member_distributor = members_roulette_probability_distributor[index - 1][1] + member_probability
                member_probability_distributor.append(member_distributor)

            members_roulette_probability_distributor.append(member_probability_distributor)

        print(members_roulette_probability_distributor)

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
    def best_fit_members_selection(
        population_to_select_from,
        best_members_selection_percentage,
        population_size
    ):
        population_to_select_from_members = population_to_select_from.get_members()
        sorted_population = Selection.sort_members_by_fit_function(population_to_select_from_members)
        last_best_member_index = math.floor(population_size * best_members_selection_percentage / 100)

        # get the best members from stack
        return sorted_population[0:last_best_member_index]

    @staticmethod
    def sort_members_by_fit_function(population_to_be_sorted):
        # sort population members in ascending order
        sorted_population = sorted(
            population_to_be_sorted,
            key=lambda member: member.get_fitness_function_val()
        )
        return sorted_population
