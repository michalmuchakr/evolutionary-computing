import random
from abc import ABC, abstractmethod


class Crossing:
    member_after_crossing_one_point = []

    def __init__(self, list_of_object_gens, probability, size, elite_members_amount):
        self.list_of_object_gens = list_of_object_gens
        self.list_of_individuals_after_selection = []
        self.probability = probability
        self.size = size
        self.elite_members_amount = elite_members_amount

        for gen_item in self.list_of_object_gens:
            self.list_of_individuals_after_selection.append(gen_item.binary_gens)

    def one_point_crossing(self, place_of_crossing, binary_value_for_the_draw_of_one,
                           binary_value_for_the_draw_of_second):
        first_chromosome_first_chunk = binary_value_for_the_draw_of_one[0][0:place_of_crossing] + \
                                       binary_value_for_the_draw_of_second[0][place_of_crossing:]
        first_chromosome_second_chunk = binary_value_for_the_draw_of_one[1][0:place_of_crossing] + \
                                        binary_value_for_the_draw_of_second[1][place_of_crossing:]

        second_chromosome_first_chunk = binary_value_for_the_draw_of_second[0][0:place_of_crossing] + \
                                        binary_value_for_the_draw_of_one[0][place_of_crossing:]
        second_chromosome_second_chunk = binary_value_for_the_draw_of_second[1][0:place_of_crossing] + \
                                         binary_value_for_the_draw_of_one[1][place_of_crossing:]

        self.member_after_crossing_one_point.append([first_chromosome_first_chunk, first_chromosome_second_chunk])
        self.member_after_crossing_one_point.append([second_chromosome_first_chunk, second_chromosome_second_chunk])

    def two_point_crossing(self, first_half_of_the_crossing_site, second_half_of_the_crossing_site,
                           binary_value_for_the_draw_of_one, binary_value_for_the_draw_of_second):
        first_chromosome_first_chunk = binary_value_for_the_draw_of_one[0][0:first_half_of_the_crossing_site] + \
                                       binary_value_for_the_draw_of_second[0][
                                       first_half_of_the_crossing_site:second_half_of_the_crossing_site] + \
                                       binary_value_for_the_draw_of_one[0][second_half_of_the_crossing_site:]
        first_chromosome_second_chunk = binary_value_for_the_draw_of_one[1][0:first_half_of_the_crossing_site] + \
                                        binary_value_for_the_draw_of_second[1][
                                        first_half_of_the_crossing_site:second_half_of_the_crossing_site] + \
                                        binary_value_for_the_draw_of_one[1][second_half_of_the_crossing_site:]

        second_chromosome_first_chunk = binary_value_for_the_draw_of_second[0][0:first_half_of_the_crossing_site] + \
                                        binary_value_for_the_draw_of_one[0][
                                        first_half_of_the_crossing_site:second_half_of_the_crossing_site] + \
                                        binary_value_for_the_draw_of_second[0][second_half_of_the_crossing_site:]
        second_chromosome_second_chunk = binary_value_for_the_draw_of_second[1][0:first_half_of_the_crossing_site] + \
                                         binary_value_for_the_draw_of_one[1][
                                         first_half_of_the_crossing_site:second_half_of_the_crossing_site] + \
                                         binary_value_for_the_draw_of_second[1][second_half_of_the_crossing_site:]

        self.member_after_crossing_one_point.append([first_chromosome_first_chunk, first_chromosome_second_chunk])
        self.member_after_crossing_one_point.append([second_chromosome_first_chunk, second_chromosome_second_chunk])

    def three_point_crossing(self, first_half_of_the_crossing_site_three_point,
                             second_half_of_the_crossing_site_three_point, third_half_of_the_crossing_site_three_point,
                             binary_value_for_the_draw_of_one, binary_value_for_the_draw_of_second):
        first_chromosome_first_chunk = binary_value_for_the_draw_of_one[0][
                                       0:first_half_of_the_crossing_site_three_point] + \
                                       binary_value_for_the_draw_of_second[0][
                                       first_half_of_the_crossing_site_three_point:second_half_of_the_crossing_site_three_point] + \
                                       binary_value_for_the_draw_of_one[0][
                                       second_half_of_the_crossing_site_three_point:third_half_of_the_crossing_site_three_point] + \
                                       binary_value_for_the_draw_of_second[0][
                                       third_half_of_the_crossing_site_three_point:]
        first_chromosome_second_chunk = binary_value_for_the_draw_of_one[1][
                                        0:first_half_of_the_crossing_site_three_point] + \
                                        binary_value_for_the_draw_of_second[1][
                                        first_half_of_the_crossing_site_three_point:second_half_of_the_crossing_site_three_point] + \
                                        binary_value_for_the_draw_of_one[1][
                                        second_half_of_the_crossing_site_three_point:third_half_of_the_crossing_site_three_point] + \
                                        binary_value_for_the_draw_of_second[1][
                                        third_half_of_the_crossing_site_three_point:]

        second_chromosome_first_chunk = binary_value_for_the_draw_of_one[0][
                                        0:first_half_of_the_crossing_site_three_point] + \
                                        binary_value_for_the_draw_of_second[0][
                                        first_half_of_the_crossing_site_three_point:second_half_of_the_crossing_site_three_point] + \
                                        binary_value_for_the_draw_of_one[0][
                                        second_half_of_the_crossing_site_three_point:third_half_of_the_crossing_site_three_point] + \
                                        binary_value_for_the_draw_of_second[0][
                                        third_half_of_the_crossing_site_three_point:]
        second_chromosome_second_chunk = binary_value_for_the_draw_of_one[1][
                                         0:first_half_of_the_crossing_site_three_point] + \
                                         binary_value_for_the_draw_of_second[1][
                                         first_half_of_the_crossing_site_three_point:second_half_of_the_crossing_site_three_point] + \
                                         binary_value_for_the_draw_of_one[1][
                                         second_half_of_the_crossing_site_three_point:third_half_of_the_crossing_site_three_point] + \
                                         binary_value_for_the_draw_of_second[1][
                                         third_half_of_the_crossing_site_three_point:]

        self.member_after_crossing_one_point.append([first_chromosome_first_chunk, first_chromosome_second_chunk])
        self.member_after_crossing_one_point.append([second_chromosome_first_chunk, second_chromosome_second_chunk])

    def call_crossover_functions(self, which_function):
        # print(self.member_after_crossing_one_point)

        while len(self.member_after_crossing_one_point) != self.size - self.elite_members_amount:

            # losuje 2 osobnikow do krzyzowania
            first_draw = random.randint(0, len(self.list_of_individuals_after_selection) - 1)
            second_draw = random.randint(0, len(self.list_of_individuals_after_selection) - 1)

            while first_draw == second_draw:
                second_draw = random.randint(0, len(self.list_of_individuals_after_selection))

            crossover_probability = random.uniform(0, 1)
            if crossover_probability < self.probability:
                # print('we will be able to cross', crossover_probability)
                # we draw the place of crossing, i.e. a number from 1 to 25
                # for one
                place_of_crossing = random.randint(1, 20)
                # for two
                first_half_of_the_crossing_site = random.randint(1, 9)
                second_half_of_the_crossing_site = random.randint(12, 20)
                # for three
                first_half_of_the_crossing_site_three_point = random.randint(1, 8)
                second_half_of_the_crossing_site_three_point = random.randint(9, 16)
                third_half_of_the_crossing_site_three_point = random.randint(17, 25)

                binary_value_for_the_draw_of_one = []
                binary_value_for_the_draw_of_second = []

                for x, obj in enumerate(self.list_of_individuals_after_selection):
                    if first_draw == x:
                        binary_value_for_the_draw_of_one = obj
                    elif second_draw == x:
                        binary_value_for_the_draw_of_second = obj

                if which_function == 1:
                    self.one_point_crossing(place_of_crossing, binary_value_for_the_draw_of_one,
                                            binary_value_for_the_draw_of_second)
                elif which_function == 2:
                    self.two_point_crossing(first_half_of_the_crossing_site, second_half_of_the_crossing_site,
                                            binary_value_for_the_draw_of_one, binary_value_for_the_draw_of_second)
                elif which_function == 3:
                    self.three_point_crossing(first_half_of_the_crossing_site_three_point,
                                              second_half_of_the_crossing_site_three_point,
                                              third_half_of_the_crossing_site_three_point,
                                              binary_value_for_the_draw_of_one,
                                              binary_value_for_the_draw_of_second)
                else:
                    break
            else:
                pass


class CrossingStrategy(ABC):
    @abstractmethod
    def cross(self, members, probability):
        pass


def get_genes_crossed_one_point(member, next_member, crossing_point, gene_x_index):
    return member.binary_gens[gene_x_index][:crossing_point] \
           + next_member.binary_gens[gene_x_index][crossing_point:]


def cross_item_one_point(member, next_member):
    crossing_point = random.randint(0, len(member.binary_gens[0]) - 1)

    return [
        get_genes_crossed_one_point(member, next_member, crossing_point, 0),
        get_genes_crossed_one_point(member, next_member, crossing_point, 1),
    ]


class OnePointCrossing(CrossingStrategy):
    def cross(self, members, probability):
        return [cross_item_one_point(
            members[chromosome_index],
            members[chromosome_index + 1]
        ) for chromosome_index in range(0, len(members), 2)] + \
               [cross_item_one_point(
                   members[chromosome_index + 1],
                   members[chromosome_index]
               ) for chromosome_index in range(0, len(members), 2)] + \
               [member.binary_gens for member in members]
