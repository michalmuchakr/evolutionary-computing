from population import Population


class EvolutionaryComputing:
    # Class that will trigger Evolutionary Computing calculation

    def __init__(self, epoch_amount, population_size, range_from, range_to):
        # init defaults
        self.__population = Population(population_size)
        self.__epoch_amount = epoch_amount
        self.__range_from = range_from
        self.__range_to = range_to

        # calculation trigger
        self.trigger_calculations()

    def trigger_calculations(self):
        self.__population.generate_random_population(self.__range_from, self.__range_to)

    @staticmethod
    def __fitness_function(x, y):
        return (1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x ** 2 - 14 * y + 6 * x * y + 3 * y ** 2)) \
               * (30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * x ** 2 + 48 * y - 36 * x * y + 27 * y ** 2))


Calculation = EvolutionaryComputing(10, 10, -2.0000, 2.0000)
Calculation.trigger_calculations()
