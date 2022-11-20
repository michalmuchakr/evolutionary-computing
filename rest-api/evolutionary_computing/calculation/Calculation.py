from Population import Population
from evolutionary_computing.calculation.crorrsing import OnePointCrossing
from evolutionary_computing.calculation.functions.goldstein_price import goldstein_price
from evolutionary_computing.calculation.selection import RouletteSelection


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
        elite_percentage,
        best_members_selection_percentage,
        tournament_selection_groups_size,
        probability_of_mutation,
        selection=RouletteSelection(),
        crossing=OnePointCrossing(),
        fitness=goldstein_price
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
        self.population = Population(population_size, selection)
        self.epoch_amount = epoch_amount
        self.search_result_range_from = search_result_range_from
        self.search_result_range_to = search_result_range_to
        self.elite_percentage = elite_percentage
        self.best_percentage_selection_members = best_members_selection_percentage
        self.probability_of_mutation = probability_of_mutation
        self.tournament_selection_groups_size = tournament_selection_groups_size
        self.crossing = crossing
        self.fitness = fitness

    def trigger(self):
        self.population.generate(self.search_result_range_from, self.search_result_range_to)
        self.population.evolve(
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
        )
