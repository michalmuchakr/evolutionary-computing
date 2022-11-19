import random

class Inversion:
    def __init__(self, probability):
        self.probability = probability
        self.inverted_population = []

    @staticmethod
    def inversion(array, probability, index_element, chromosome_index):
        """
        Attributes:
            array: array of any values'
            probability: probability of inversion (float)
        """
        # TODO check if genes shoul be equal
        if random.random() > probability: return array

        start = random.randint(0, len(array) - 1)
        end = random.randint(start + 1, len(array))

        fragment = array[start:end][::-1]
        return array[0:start] + fragment + array[end:]

    def inversion_in_population(self, population_after_mutation):
        self.inverted_population = [
            [self.inversion(chromosome[index_element], self.probability, index_element, chromosome_index)
                for index_element in range(2)]
            for chromosome_index, chromosome in enumerate(population_after_mutation)
        ]
