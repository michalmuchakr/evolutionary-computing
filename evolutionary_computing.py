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

        # percentage the best members picked in selection
        best_members_selection_percentage,

        # population chunks size while select tournament
        tournament_selection_groups_size
    ):
        self.population = Population(population_size)
        self.epoch_amount = epoch_amount
        self.search_result_range_from = search_result_range_from
        self.search_result_range_to = search_result_range_to
        self.best_percentage_selection_members = best_members_selection_percentage
        self.tournament_selection_groups_size = tournament_selection_groups_size

        # calculation trigger
        self.trigger_initial_calculations()

    def trigger_initial_calculations(self):
        self.population.generate_random_population(
            self.search_result_range_from,
            self.search_result_range_to,
        )

        # selected_from_population = Selection.get_best_members_by_fit_function_by_percentage(
        #     self.population,
        #     best_members_selection_percentage,
        #     population_size
        # )

        # selected_from_population = Selection.tournament_members_selection(
        #     self.population,
        #     self.tournament_selection_groups_size
        # )

        selected_from_population = Selection.roulette_wheel_members_selection(self.population)

        self.population.set_selected_from_population(selected_from_population)


Calculation = EvolutionaryComputing(10, 10, -2.0000, 2.0000, 3, 2)
Calculation.trigger_initial_calculations()
