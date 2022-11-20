from .crorrsing import OnePointCrossing
from .functions.goldstein_price import goldstein_price
from .mutation import HomogeneousMutation, EdgeMutation, TwoPointMutation
from .population import Population
from .selection import RouletteSelection, TournamentSelection


class Calculation:
    """
    Class for Evolutionary Computing calculation
    """

    selection_dictionary = {
        "roulette": RouletteSelection(),
        "best": RouletteSelection(),
        "tournament": TournamentSelection(),
    }

    crossing_dictionary = {
        "one_point": OnePointCrossing(),
        "two_points": OnePointCrossing(),
        "three_points": OnePointCrossing(),
        "homo": OnePointCrossing()
    }

    mutation_dictionary = {
        "homogeneous_mutation": HomogeneousMutation(),
        "edge_mutation": EdgeMutation(),
        "two_point_mutation": TwoPointMutation(),
    }

    fit_function_dictionary = {
        "goldstein_price": goldstein_price
    }

    def __init__(
        self,
        epoch_amount,
        best_members_selection_percentage,
        population_members_count,
        search_result_range_from,
        search_result_range_to,
        elite_percentage,
        tournament_selection_groups_size,
        cross_probability,
        mutation_probability,
        inversion_probability,
        selection_method,
        problem_to_solve,
        crossing_kind,
        mutation_method,
        fit_function
    ):
        """
        Attributes:
            epoch_amount: amount of epochs in calculation
            best_members_selection_percentage: percentage the best members picked in selection
            population_members_count: amount of population members
            search_result_range_from: fit function renge start for x1 and x2
            search_result_range_to: fit function renge end for x1 and x2
            tournament_selection_groups_size: population chunks size while select tournament
            selection_method: type of selection
            mutation_method: fitness function
        """
        self.selection_kind = self.selection_dictionary[selection_method]
        self.best_percentage_selection_members = best_members_selection_percentage
        self.population = Population(population_members_count, self.selection_kind)
        self.epoch_amount = epoch_amount
        self.search_result_range_from = search_result_range_from
        self.search_result_range_to = search_result_range_to
        self.elite_percentage = elite_percentage
        self.tournament_selection_groups_size = tournament_selection_groups_size
        self.crossing = self.crossing_dictionary[crossing_kind]
        self.fitness = self.fit_function_dictionary[fit_function]
        self.problem_to_solve = problem_to_solve
        self.probability_of_mutation = mutation_probability
        self.probability_of_crossing = cross_probability
        self.probability_of_inversion = inversion_probability
        self.mutation = self.mutation_dictionary[mutation_method]

    def trigger(self):
        self.population.generate(self.search_result_range_from, self.search_result_range_to)
        return self.population.evolve(
            self.fitness,
            self.crossing,
            self.epoch_amount,
            self.elite_percentage,
            self.problem_to_solve,
            self.probability_of_mutation,
            self.probability_of_crossing,
            self.probability_of_inversion,
            self.search_result_range_from,
            self.search_result_range_to,
            self.mutation
        )
