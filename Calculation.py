from Population import Population

class Calculation:
    """
    Class for Evolutionary Computing calculation
    """

    def __init__(
        self,
        epoch_amount,
        population_size,
        search_result_range_from,
        search_result_range_to,
        best_members_selection_percentage,
        tournament_selection_groups_size,
        selection,
        fitness
    ):
        """
        Attributes:
            epoch_amount: amount of epochs in calculation
            population_size: amount of population members
            search_result_range_from: fit function renge start for x1 and x2
            search_result_range_to: fit function renge end for x1 and x2
            best_members_selection_percentage: percentage the best members picked in selection
            tournament_selection_groups_size: population chunks size while select tournament
            selection: type of selection
            fitness: fitness function
        """
        self.population = Population(population_size)
        self.epoch_amount = epoch_amount
        self.search_result_range_from = search_result_range_from
        self.search_result_range_to = search_result_range_to
        self.best_percentage_selection_members = best_members_selection_percentage
        self.tournament_selection_groups_size = tournament_selection_groups_size
        self._selection = selection
        self.fitness = fitness

    def trigger(self):
        self.population.generate_random_population(
            self.search_result_range_from,
            self.search_result_range_to,
        )

        selected = self._selection.select(self.population)

        # self.population.set_selected_from_population(selected_from_population)
