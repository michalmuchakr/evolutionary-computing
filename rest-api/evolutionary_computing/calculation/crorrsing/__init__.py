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

def getGenesArithmeticCrossoverX1X2Y1Y2(x1, y1, x2,y2):
    returnX1Y1 = []
    for num,x1 in enumerate(x1):
        k_parameter = random.random()
        returnX1Y1.append([k_parameter * x1 + (1-k_parameter) * x2[num],k_parameter * y1[num] + (1-k_parameter) * y2[num]])
        returnX1Y1.append([(1 - k_parameter) * x1 + k_parameter * x2[num], (1 - k_parameter) * y1[num] + k_parameter * y2[num]])
    return returnX1Y1

def arithmeticCrossover(x1,y1,x2,y2):
    return getGenesArithmeticCrossoverX1X2Y1Y2(x1, y1, x2,y2)

def blendCrossoverXY(x1,y1,x2,y2,alfa):
    returnX1Y1 = []
    for num,x1 in enumerate(x1):
        returnX1Y1.append([random.uniform((min(x1,x2[num])-alfa*abs(x1-x2[num])),max(x1,x2[num])+alfa*abs(x1-x2[num])),\
                           random.uniform((min(x1,x2[num])-alfa*abs(x1-x2[num])),max(x1,x2[num])+alfa*abs(x1-x2[num]))])
        returnX1Y1.append([random.uniform((min(y1[num],y2[num])-alfa*abs(x1-x2[num])),max(x1,x2[num])+alfa*abs(x1-x2[num])),\
                           random.uniform((min(y1[num],y2[num])-alfa*abs(x1-x2[num])),max(x1,x2[num])+alfa*abs(x1-x2[num]))])

    return returnX1Y1

def blendCrossoverXYBeta(x1,y1,x2,y2,alfa,beta):
    returnX1Y1 = []
    for num,x1 in enumerate(x1):
        returnX1Y1.append([random.uniform((min(x1,x2[num])-alfa*abs(x1-x2[num])),max(x1,x2[num])+beta*abs(x1-x2[num])),\
                           random.uniform((min(x1,x2[num])-alfa*abs(x1-x2[num])),max(x1,x2[num])+beta*abs(x1-x2[num]))])
        returnX1Y1.append([random.uniform((min(y1[num],y2[num])-alfa*abs(x1-x2[num])),max(x1,x2[num])+beta*abs(x1-x2[num])),\
                           random.uniform((min(y1[num],y2[num])-alfa*abs(x1-x2[num])),max(x1,x2[num])+beta*abs(x1-x2[num]))])

    return returnX1Y1

def averageCrossoverXY(x1,y1,x2,y2):
    returnX1Y1 = []
    for num,x1 in enumerate(x1):
        xd = random.uniform(0.01,0.2)
        returnX1Y1.append([(x1+x2[num])/2 , (y1[num]+y2[num])/2])
        returnX1Y1.append([(x1+x2[num]-xd)/2 , (y1[num]+y2[num]-xd)/2])

    return returnX1Y1






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

class ArithmeticCrossover(CrossingStrategy):
    def cross(self, members, probability, problem_to_solve):

        x1,x2 = ([members.dec_gens[0] for numb, members in enumerate(members) if numb % 2 == 0],[members.dec_gens[0] for numb,members in enumerate(members) if numb%2!=0])
        y1, y2 = ([members.dec_gens[1] for numb, members in enumerate(members) if numb % 2 == 0],
                  [members.dec_gens[1] for numb, members in enumerate(members) if numb % 2 != 0])

        return arithmeticCrossover(x1,y1,x2,y2) + arithmeticCrossover(x1,y1,x2,y2)

class BlendCrossover(CrossingStrategy):
    def cross(self, members, probability, problem_to_solve):

        x1,x2 = ([members.dec_gens[0] for numb, members in enumerate(members) if numb % 2 == 0],[members.dec_gens[0] for numb,members in enumerate(members) if numb%2!=0])
        y1, y2 = ([members.dec_gens[1] for numb, members in enumerate(members) if numb % 2 == 0],
                  [members.dec_gens[1] for numb, members in enumerate(members) if numb % 2 != 0])
        alfa = 0.25

        return blendCrossoverXY(x1,y1,x2,y2,alfa) + blendCrossoverXY(x1,y1,x2,y2,alfa)

class BlendCrossoverBeta(CrossingStrategy):
    def cross(self, members, probability, problem_to_solve):

        x1,x2 = ([members.dec_gens[0] for numb, members in enumerate(members) if numb % 2 == 0],[members.dec_gens[0] for numb,members in enumerate(members) if numb%2!=0])
        y1, y2 = ([members.dec_gens[1] for numb, members in enumerate(members) if numb % 2 == 0],
                  [members.dec_gens[1] for numb, members in enumerate(members) if numb % 2 != 0])
        alfa = 0.25
        beta = 0.7

        return blendCrossoverXYBeta(x1,y1,x2,y2,alfa,beta) + blendCrossoverXYBeta(x1,y1,x2,y2,alfa,beta)

class AverageCrossover(CrossingStrategy):
    def cross(self, members, probability, problem_to_solve):

        x1,x2 = ([members.dec_gens[0] for numb, members in enumerate(members) if numb % 2 == 0],[members.dec_gens[0] for numb,members in enumerate(members) if numb%2!=0])
        y1, y2 = ([members.dec_gens[1] for numb, members in enumerate(members) if numb % 2 == 0],
                  [members.dec_gens[1] for numb, members in enumerate(members) if numb % 2 != 0])

        return averageCrossoverXY(x1,y1,x2,y2) + averageCrossoverXY(x1,y1,x2,y2)

