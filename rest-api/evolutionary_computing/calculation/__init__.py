from .Population import Population
from .crorrsing import OnePointCrossing
from .functions.goldstein_price import goldstein_price
from .selection import RouletteSelection


class Calculation:
    """
    Class for Evolutionary Computing calculation
    """

    selection_dictionary = {
        "roulette": RouletteSelection(),
        "best": RouletteSelection(),
    }

    crossing_dictionary = {
        "one_point": OnePointCrossing(),
        "two_points": OnePointCrossing(),
        "three_points": OnePointCrossing(),
        "homo": OnePointCrossing()
    }

    fit_function_dictionary = {
        "goldstein_price": goldstein_price
    }

    def __init__(
        self,
        epoch_amount,
        population_size,
        search_result_range_from,
        search_result_range_to,
        elite_percentage,
        best_members_selection_percentage,
        tournament_selection_groups_size,
        selection_kind,
        problem_to_solve,
        crossing_kind,
        fitness_kind
    ):
        """
        Attributes:
            epoch_amount: amount of epochs in calculation
            population_size: amount of population members
            search_result_range_from: fit function renge start for x1 and x2
            search_result_range_to: fit function renge end for x1 and x2
            best_members_selection_percentage: percentage the best members picked in selection
            tournament_selection_groups_size: population chunks size while select tournament
            selection_kind: type of selection
            fitness_kind: fitness function
        """
        self.selection_kind = self.selection_dictionary[selection_kind]
        self.population = Population(population_size, self.selection_kind)
        self.epoch_amount = epoch_amount
        self.search_result_range_from = search_result_range_from
        self.search_result_range_to = search_result_range_to
        self.elite_percentage = elite_percentage
        self.best_percentage_selection_members = best_members_selection_percentage
        self.tournament_selection_groups_size = tournament_selection_groups_size
        self.crossing = self.crossing_dictionary[crossing_kind]
        self.fitness = self.fit_function_dictionary[fitness_kind]
        self.problem_to_solve = problem_to_solve

    def trigger(self):
        self.population.generate(self.search_result_range_from, self.search_result_range_to)
        return self.population.evolve(
            self.fitness,
            self.crossing,
            self.epoch_amount,
            self.elite_percentage,
            self.problem_to_solve,
            self.search_result_range_from,
            self.search_result_range_to
        )
