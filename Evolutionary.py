from Population import Population
from Selection import Selection

class Evolutionary:
    # Class that will trigger Evolutionary Computing calculation

    def __init__(
        self,
        epoch_amount,
        population_size,
        search_result_range_from,
        search_result_range_to,
        best_members_selection_percentage,
        tournament_selection_groups_size,

    ):
        """
        Attributes:
            epoch_amount: amount of epochs in calculation
            population_size: amount of population members
            search_result_range_from: fit function renge start for x1 and x2
            search_result_range_to: fit function renge end for x1 and x2
            best_members_selection_percentage: percentage the best members picked in selection
            tournament_selection_groups_size: population chunks size while select tournament
        """
        self.population = Population(population_size)
        self.epoch_amount = epoch_amount
        self.search_result_range_from = search_result_range_from
        self.search_result_range_to = search_result_range_to
        self.best_percentage_selection_members = best_members_selection_percentage
        self.tournament_selection_groups_size = tournament_selection_groups_size

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


calculation = Evolutionary(10, 10, -2.0000, 2.0000, 3, 2)
calculation.trigger_initial_calculations()
