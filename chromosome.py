from fitness_function import fitness_function


class Chromosome:
    # chromosome
    __gens = []

    def __init__(self, initial_gens, fittness_function_precision):

        self.__gens = initial_gens
        self.__fitness_function_val = round(
            fitness_function(
                initial_gens[0],
                initial_gens[1]
            ),
            fittness_function_precision
        )

    def __str__(self):
        return "(" + str(self.__gens[0]) + ", " + str(self.__gens[1]) + ") = " +\
               str(self.__fitness_function_val)
