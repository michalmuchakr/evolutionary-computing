import random
from abc import ABC, abstractmethod


class MutationStrategy(ABC):
    @abstractmethod
    def mutate(self, member_after_crossing, probability_of_mutation):
        pass


class HomogeneousMutation(MutationStrategy):
    def mutate(self, member_after_crossing, probability_of_mutation):
        member_after_mutation = []
        for i in member_after_crossing:
            probability_of_mutation_tmp = random.uniform(0, 1)
            if probability_of_mutation_tmp < probability_of_mutation:
                first_draw = random.randint(1, 9)
                second_draw = random.randint(10, 20)
                first_value_before_change = i[0][first_draw]
                second_value_before_change = i[1][second_draw]

                if first_value_before_change and second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw] + [False] + i[0][first_draw + 1:],
                                                  i[1][0:second_draw] + [False] + i[1][second_draw + 1:]])
                elif first_value_before_change == False and second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw] + [True] + i[0][first_draw + 1:],
                                                  i[1][0:second_draw] + [True] + i[1][second_draw + 1:]])
                elif first_value_before_change and second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw] + [False] + i[0][first_draw + 1:],
                                                  i[1][0:second_draw] + [True] + i[1][second_draw + 1:]])
                elif first_value_before_change == False and second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw] + [True] + i[0][first_draw + 1:],
                                                  i[1][0:second_draw] + [False] + i[1][second_draw + 1:]])
            else:
                member_after_mutation.append(i)

        return member_after_mutation


class EdgeMutation(MutationStrategy):
    def mutate(self, member_after_crossing, probability_of_mutation):
        member_after_mutation = []
        for i in member_after_crossing:
            probability_of_mutation_tmp = random.uniform(0, 1)
            if probability_of_mutation_tmp < probability_of_mutation:
                edge_value = 20
                first_value_before_change = i[0][edge_value]
                second_value_before_change = i[1][edge_value]
                if first_value_before_change and second_value_before_change:
                    member_after_mutation.append([i[0][:20] + [False], i[1][:20] + [False]])
                elif first_value_before_change == False and second_value_before_change == False:
                    member_after_mutation.append([i[0][:20] + [True], i[1][:20] + [True]])
                elif first_value_before_change == False and second_value_before_change:
                    member_after_mutation.append([i[0][:20] + [True], i[1][:20] + [False]])
                elif first_value_before_change and second_value_before_change == False:
                    member_after_mutation.append([i[0][:20] + [False], i[1][:20] + [True]])
            else:
                member_after_mutation.append(i)

        return member_after_mutation


class TwoPointMutation(MutationStrategy):

    def mutate(self, member_after_crossing, probability_of_mutation):
        member_after_mutation = []
        for i in member_after_crossing:
            probability_of_mutation_tmp = random.uniform(0, 1)

            if probability_of_mutation_tmp < probability_of_mutation:
                first_draw = random.randint(2, 10)
                second_draw = random.randint(12, 18)

                first_draw_2 = random.randint(2, 10)
                second_draw_2 = random.randint(12, 18)

                first_value_before_change = i[0][first_draw]
                second_value_before_change = i[0][second_draw]

                second_first_value_before_change = i[1][first_draw_2]
                second_second_value_before_change = i[1][second_draw_2]

                if first_value_before_change == False and second_value_before_change == False and second_first_value_before_change == False and second_second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [True] + i[0][
                                                                                    first_draw:second_draw - 1] + [
                                                      True] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [True] + i[1][
                                                                                      first_draw_2:second_draw_2 - 1] + [
                                                      True] + i[1][second_draw_2:]])
                elif first_value_before_change == False and second_value_before_change == False and second_first_value_before_change == False and second_second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [True] + i[0][
                                                                                    first_draw:second_draw - 1] + [
                                                      True] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [True] + i[1][
                                                                                      first_draw_2:second_draw_2 - 1] + [
                                                      False] + i[1][second_draw_2:]])
                elif first_value_before_change == False and second_value_before_change == False and second_first_value_before_change and second_second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [True] + i[0][
                                                                                    first_draw:second_draw - 1] + [
                                                      True] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [False] + i[1][
                                                                                       first_draw_2:second_draw_2 - 1] + [
                                                      False] + i[1][second_draw_2:]])
                elif first_value_before_change == False and second_value_before_change and second_first_value_before_change and second_second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [True] + i[0][
                                                                                    first_draw:second_draw - 1] + [
                                                      False] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [False] + i[1][
                                                                                       first_draw_2:second_draw_2 - 1] + [
                                                      False] + i[1][second_draw_2:]])
                elif first_value_before_change and second_value_before_change and second_first_value_before_change and second_second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                     first_draw:second_draw - 1] + [
                                                      False] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [False] + i[1][
                                                                                       first_draw_2:second_draw_2 - 1] + [
                                                      False] + i[1][second_draw_2:]])
                elif first_value_before_change and second_value_before_change and second_first_value_before_change and second_second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                     first_draw:second_draw - 1] + [
                                                      False] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [False] + i[1][
                                                                                       first_draw_2:second_draw_2 - 1] + [
                                                      True] + i[1][second_draw_2:]])
                elif first_value_before_change and second_value_before_change and second_first_value_before_change == False and second_second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                     first_draw:second_draw - 1] + [
                                                      False] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [True] + i[1][
                                                                                      first_draw_2:second_draw_2 - 1] + [
                                                      True] + i[1][second_draw_2:]])
                elif first_value_before_change and second_value_before_change == False and second_first_value_before_change == False and second_second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                     first_draw:second_draw - 1] + [
                                                      True] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [True] + i[1][
                                                                                      first_draw_2:second_draw_2 - 1] + [
                                                      True] + i[1][second_draw_2:]])
                elif first_value_before_change == False and second_value_before_change and second_first_value_before_change == False and second_second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                     first_draw:second_draw - 1] + [
                                                      False] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [True] + i[1][
                                                                                      first_draw_2:second_draw_2 - 1] + [
                                                      True] + i[1][second_draw_2:]])
                elif first_value_before_change == False and second_value_before_change == False and second_first_value_before_change and second_second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [True] + i[0][
                                                                                    first_draw:second_draw - 1] + [
                                                      True] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [False] + i[1][
                                                                                       first_draw_2:second_draw_2 - 1] + [
                                                      True] + i[1][second_draw_2:]])
                elif first_value_before_change == False and second_value_before_change and second_first_value_before_change and second_second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [True] + i[0][
                                                                                    first_draw:second_draw - 1] + [
                                                      False] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [False] + i[1][
                                                                                       first_draw_2:second_draw_2 - 1] + [
                                                      True] + i[1][second_draw_2:]])
                elif first_value_before_change and second_value_before_change == False and second_first_value_before_change == False and second_second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                     first_draw:second_draw - 1] + [
                                                      True] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [True] + i[1][
                                                                                      first_draw_2:second_draw_2 - 1] + [
                                                      False] + i[1][second_draw_2:]])
                elif first_value_before_change and second_value_before_change == False and second_first_value_before_change and second_second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                     first_draw:second_draw - 1] + [
                                                      True] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [False] + i[1][
                                                                                       first_draw_2:second_draw_2 - 1] + [
                                                      False] + i[1][second_draw_2:]])
                elif first_value_before_change and second_value_before_change and second_first_value_before_change == False and second_second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                     first_draw:second_draw - 1] + [
                                                      False] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [True] + i[1][
                                                                                      first_draw_2:second_draw_2 - 1] + [
                                                      False] + i[1][second_draw_2:]])
                elif first_value_before_change == False and second_value_before_change and second_first_value_before_change == False and second_second_value_before_change:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [True] + i[0][
                                                                                    first_draw:second_draw - 1] + [
                                                      False] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [True] + i[1][
                                                                                      first_draw_2:second_draw_2 - 1] + [
                                                      False] + i[1][second_draw_2:]])
                elif first_value_before_change and second_value_before_change == False and second_first_value_before_change and second_second_value_before_change == False:
                    member_after_mutation.append([i[0][0:first_draw - 1] + [False] + i[0][
                                                                                     first_draw:second_draw - 1] + [
                                                      True] + i[0][second_draw:],
                                                  i[1][0:first_draw_2 - 1] + [False] + i[1][
                                                                                       first_draw_2:second_draw_2 - 1] + [
                                                      True] + i[1][second_draw_2:]])


            else:
                member_after_mutation.append(i)
        return member_after_mutation
