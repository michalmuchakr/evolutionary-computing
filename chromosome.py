class Chromosome:
    # chromosome
    gens = []
    fit_function_value = 0

    def __init__(self, initial_gens):
        self.gens = initial_gens

    def __str__(self):
        print("chromosome x1(" + self.gens[0] + "," + self.gens[1] + " = " + self.fit_function_value)
