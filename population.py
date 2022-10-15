from chromosome import Chromosome


class Population:
    # population
    members = []
    selected_from_population = []

    def __init__(self, population_size):
        self.population_size = population_size

    def len(self):
        return self.population_size

    def set_selected_from_population(self, selected_from_population):
        self.selected_from_population = selected_from_population

    def get_members(self):
        return self.members

    def generate_random_population(
        self,
        search_result_range_from,
        search_result_range_to,
    ):
        chromosome_len = Chromosome.get_chromosome_len(search_result_range_from, search_result_range_to)

        for member in range(self.population_size):
            generated_chromosome = Chromosome(
                search_result_range_from, search_result_range_to, chromosome_len)

            self.members.append(generated_chromosome)

    def print_population(self):
        for member in self.members:
            print(member)

    def print_selected_from_population(self):
        for member in self.selected_from_population:
            print(member)

    def str(self):
        return "Population size: " + self.population_size
