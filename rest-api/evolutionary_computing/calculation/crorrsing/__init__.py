import random
from abc import ABC, abstractmethod


class CrossingStrategy(ABC):
    @abstractmethod
    def cross(self, members, probability, problem_to_solve):
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


def get_genes_crossed_two_point(member, next_member, crossing_points, gene_x_index):
    if crossing_points[0] < crossing_points[1]:
        return member.binary_gens[gene_x_index][:crossing_points[0]] \
               + next_member.binary_gens[gene_x_index][crossing_points[0]:crossing_points[1]] + member.binary_gens[
                                                                                                    gene_x_index][
                                                                                                crossing_points[1]:]
    else:
        return member.binary_gens[gene_x_index][:crossing_points[1]] \
               + next_member.binary_gens[gene_x_index][crossing_points[1]:crossing_points[0]] + member.binary_gens[
                                                                                                    gene_x_index][
                                                                                                crossing_points[0]:]


def cross_item_two_point(member, next_member):
    crossing_point = list(range(0, len(member.binary_gens[0]) - 1))
    crossing_points = random.sample(crossing_point, k=2)

    return [
        get_genes_crossed_two_point(member, next_member, crossing_points, 0),
        get_genes_crossed_two_point(member, next_member, crossing_points, 1)
    ]


def get_genes_crossed_three_point(member, next_member, crossing_points, gene_x_index):
    return member.binary_gens[gene_x_index][:crossing_points[0]] \
           + next_member.binary_gens[gene_x_index][crossing_points[0]:crossing_points[1]] \
           + member.binary_gens[gene_x_index][crossing_points[1]:crossing_points[2]] \
           + member.binary_gens[gene_x_index][crossing_points[2]:]


def cross_item_three_point(member, next_member):
    crossing_point = list(range(0, len(member.binary_gens[0]) - 1))
    crossing_points = random.sample(crossing_point, k=3)
    crossing_points.sort()

    return [
        get_genes_crossed_three_point(member, next_member, crossing_points, 0),
        get_genes_crossed_three_point(member, next_member, crossing_points, 1)
    ]


def get_genes_crossed_homo_point(member, next_member, gene_x_index):
    homo_list = []

    for actualNumber, binary_member in enumerate(member.binary_gens[gene_x_index]):
        if actualNumber % 2:
            homo_list.append(binary_member)
        else:
            homo_list.append(next_member.binary_gens[gene_x_index][actualNumber])

    return homo_list


def cross_item_homo_point(member, next_member):
    co_to = get_genes_crossed_homo_point(member, next_member, 0)

    return [
        get_genes_crossed_homo_point(member, next_member, 0),
        get_genes_crossed_homo_point(member, next_member, 1)
    ]


class OnePointCrossing(CrossingStrategy):
    def cross(self, members, probability, problem_to_solve):
        return \
            [cross_item_one_point(
                members[chromosome_index],
                members[chromosome_index + 1]
            ) for chromosome_index in range(0, len(members), 2)] + \
            [cross_item_one_point(
                members[chromosome_index + 1],
                members[chromosome_index]
            ) for chromosome_index in range(0, len(members), 2)] + \
            [member.binary_gens for member in members]


class OneTwoPointsCrossing(CrossingStrategy):
    def cross(self, members, probability, problem_to_solve):
        return \
            [cross_item_two_point(
                members[chromosome_index],
                members[chromosome_index + 1]
            ) for chromosome_index in range(0, len(members), 2)] + \
            [cross_item_two_point(
                members[chromosome_index + 1],
                members[chromosome_index]
            ) for chromosome_index in range(0, len(members), 2)] + \
            [member.binary_gens for member in members]


class OneThreePointsCrossing(CrossingStrategy):
    def cross(self, members, probability, problem_to_solve):
        return \
            [cross_item_three_point(
                members[chromosome_index],
                members[chromosome_index + 1]
            ) for chromosome_index in range(0, len(members), 2)] + \
            [cross_item_three_point(
                members[chromosome_index + 1],
                members[chromosome_index]
            ) for chromosome_index in range(0, len(members), 2)] + \
            [member.binary_gens for member in members]


class HomoCrossing(CrossingStrategy):
    def cross(self, members, probability, problem_to_solve):
        return \
            [cross_item_homo_point(
                members[chromosome_index],
                members[chromosome_index + 1]
            ) for chromosome_index in range(0, len(members), 2)] + \
            [cross_item_homo_point(
                members[chromosome_index + 1],
                members[chromosome_index]
            ) for chromosome_index in range(0, len(members), 2)] + \
            [member.binary_gens for member in members]
