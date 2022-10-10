from population import Population
from selection import Selection


class EvolutionaryComputing:
    # Class that will trigger Evolutionary Computing calculation

    def __init__(
        self,
        # amount of epochs in calculation
        epoch_amount,

        # amount of population members
        population_size,

        # fit function renge start for x1 and x2
        search_result_range_from,

        # fit function renge end for x1 and x2
        search_result_range_to,

        # decimal precision
        chromosome_gens_precision,
        fittness_function_precision,

        # percentage the best members picked in selection
        best_members_selection_percentage,

        #
        tournament_selection_groups_size
    ):
        self.__population = Population(population_size)
        self.__epoch_amount = epoch_amount
        self.__search_result_range_from = search_result_range_from
        self.__search_result_range_to = search_result_range_to
        self.__chromosome_gens_precision = chromosome_gens_precision
        self.__fittness_function_precision = fittness_function_precision
        self.__best_percentage_selection_members = best_members_selection_percentage
        self.__tournament_selection_groups_size = tournament_selection_groups_size

        # calculation trigger
        self.trigger_initial_calculations()

        # selected_from_population = Selection.get_best_members_by_fit_function_by_percentage(
        #     self.__population,
        #     best_members_selection_percentage,
        #     population_size
        # )

        selected_from_population = Selection.tournament_members_selection(
            self.__population,
            tournament_selection_groups_size
        )

        self.__population.set_selected_from_population(selected_from_population)

        self.__population.print_population()
        print()
        self.__population.print_selected_from_population()

    def trigger_initial_calculations(self):
        self.__population.generate_random_population(
            self.__search_result_range_from,
            self.__search_result_range_to,
            self.__chromosome_gens_precision,
            self.__fittness_function_precision
        )


Calculation = EvolutionaryComputing(100, 100, -2.0000, 2.0000, 4, 4, 30, 7)
Calculation.trigger_initial_calculations()
