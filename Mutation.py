import random

class Mutation:
    member_after_mutation = []
    def __init__(self,member_after_crossing,probability_of_mutation):
        self.member_after_crossing = member_after_crossing
        self.probability_of_mutation = probability_of_mutation

    def homogeneous_mutation(self):
        for i in self.member_after_crossing:
            probability_of_mutation_tmp = random.uniform(0, 1)
            if probability_of_mutation_tmp < self.probability_of_mutation:
                first_draw = random.randint(1,20)
                first_value_before_change = i[0][first_draw]

                if first_value_before_change == True:
                    self.member_after_mutation.append([i[0][0:first_draw]+[False]+i[0][first_draw+1:],i[1][0:first_draw] + [False] + i[1][first_draw + 1:]])
                else:
                    self.member_after_mutation.append([i[0][0:first_draw]+[True]+i[0][first_draw+1:],i[1][0:first_draw] + [True] + i[1][first_draw + 1:]])
            else:
                self.member_after_mutation.append(i)

    def edge_mutation(self):

        for i in self.member_after_crossing:
            probability_of_mutation_tmp = random.uniform(0, 1)
            if probability_of_mutation_tmp < self.probability_of_mutation:
                edge_value = 20
                first_value_before_change = i[0][edge_value]
                if first_value_before_change == True:
                    self.member_after_mutation.append([i[0][:19] + [False], i[1][:19] + [False]])
                else:
                    self.member_after_mutation.append([i[0][:19] + [True], i[1][:19] + [True]])
            else:
                self.member_after_mutation.append(i)

    def two_point_mutation(self):

        for i in self.member_after_crossing:
            probability_of_mutation_tmp = random.uniform(0, 1)

            if probability_of_mutation_tmp < self.probability_of_mutation:
                first_draw = random.randint(2,10)
                second_draw = random.randint(12,18)

                first_value_before_change = i[0][first_draw]
                second_value_before_change = i[0][second_draw]

                if first_value_before_change == False:
                    self.member_after_mutation.append([i[0][0:first_draw-1] + [True] + i[0][first_draw:second_draw-1] + [True] + i[0][second_draw:],i[1][0:first_draw-1] + [True] + i[1][first_draw:second_draw-1] + [True] + i[1][second_draw:]])
                else:
                    self.member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                         first_draw:second_draw - 1] + [
                                                           False] + i[0][second_draw:],i[1][0:first_draw-1] + [False] + i[1][first_draw:second_draw-1] + [False] + i[1][second_draw:]])

            else:
                self.member_after_mutation.append(i)
