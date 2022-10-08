from population import Population


class EvolutionaryComputing:
    # Class that will trigger Evolutionary Computing calculation

    def __init__(
        self,
        epoch_amount,
        population_size,
        search_result_range_from,
        search_result_range_to,
        chromosome_gens_precision,
        fittness_function_precision
    ):
        self.__population = Population(population_size)
        self.__epoch_amount = epoch_amount
        self.__search_result_range_from = search_result_range_from
        self.__search_result_range_to = search_result_range_to
        self.__chromosome_gens_precision = chromosome_gens_precision
        self.__fittness_function_precision = fittness_function_precision

        # calculation trigger
        self.trigger_calculations()
        self.__population.print_population()

    def trigger_calculations(self):
        self.__population.generate_random_population(
            self.__search_result_range_from,
            self.__search_result_range_to,
            self.__chromosome_gens_precision,
            self.__fittness_function_precision
        )


Calculation = EvolutionaryComputing(10, 10, -2.0000, 2.0000, 4, 4)
Calculation.trigger_calculations()
