import math


class Selection:
    # Selection algorithms

    @staticmethod
    def get_best_members_by_fit_function_by_percentage(
        population_to_select_members,
        best_members_selection_percentage,
        population_size
    ):
        sorted_population = Selection.sort_members_by_fit_function(population_to_select_members)
        last_best_member_index = math.floor(population_size * best_members_selection_percentage / 100)

        return sorted_population[0:last_best_member_index]

    @staticmethod
    def sort_members_by_fit_function(population_to_be_sorted):
        # sort population members in ascending order
        sorted_population = sorted(
            population_to_be_sorted.get_members(),
            key=lambda member: member.get_fitness_function_val()
        )
        return sorted_population
