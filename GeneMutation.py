import random

from CrossingGens import Osobnik_po_selekcji
os1 = Osobnik_po_selekcji(1,1111,'dsfasdf','dadfsa')

class GeneMutation:
    member_after_mutation = []

    def __init__(self,list_of_object_gens,probability_of_mutation):
        self.list_of_object_gens = list_of_object_gens
        self.list_of_individuals_after_selection = []
        self.probability_of_mutation = probability_of_mutation

        for x in list_of_object_gens:
            self.list_of_individuals_after_selection.append(x.reprezentacja_binarna)


    def homogeneous_mutation(self):

        for i in self.list_of_individuals_after_selection:

            probability_of_mutation_tmp = random.uniform(0, 1)
            if probability_of_mutation_tmp < self.probability_of_mutation:
                first_draw = random.randint(0, len(self.list_of_individuals_after_selection) - 1)
                value_before_change = i[first_draw]

                if value_before_change == '0':
                    self.member_after_mutation.append(
                        i[0:first_draw] + '1' + i[first_draw:26])
                else:
                    self.member_after_mutation.append(
                        i[0:first_draw] + '0' + i[first_draw:26])
            else:
                self.member_after_mutation.append(i)

    def two_point_mutation(self):

        for i in self.list_of_individuals_after_selection:
            if len(self.member_after_mutation) >= 10:
                break

            probability_of_mutation_tmp = random.uniform(0, 1)
            if probability_of_mutation_tmp < self.probability_of_mutation:
                first_draw = random.randint(0, len(self.list_of_individuals_after_selection) - 1)
                second_draw = random.randint(0, len(self.list_of_individuals_after_selection) - 1)

                while (first_draw == second_draw):
                    second_draw = random.randint(0, len(self.list_of_individuals_after_selection))

                first_value_before_change = i[first_draw]
                second_value_before_change = i[second_draw]

                if first_value_before_change == '0':
                    if len(self.member_after_mutation) >= 10:
                        break
                    self.member_after_mutation.append(
                        i[0:first_draw] + '1' + i[first_draw:26])
                else:
                    if len(self.member_after_mutation) >= 10:
                        break
                    self.member_after_mutation.append(
                        i[0:first_draw] + '0' + i[first_draw:26])

                if second_value_before_change == '0':
                    if len(self.member_after_mutation) >= 10:
                        break
                    self.member_after_mutation.append(
                        i[0:second_draw] + '1' + i[second_draw:26])
                else:
                    if len(self.member_after_mutation) >= 10:
                        break
                    self.member_after_mutation.append(
                        i[0:second_draw] + '0' + i[second_draw:26])
            else:
                if len(self.member_after_mutation) >= 10:
                    break
                self.member_after_mutation.append(i)

    def edge_mutation(self):

        for i in self.list_of_individuals_after_selection:
            probability_of_mutation_tmp = random.uniform(0, 1)
            if probability_of_mutation_tmp < self.probability_of_mutation:
                edge_value = len(i) - 1
                value_before_change = i[edge_value]
                if value_before_change == '0':
                    self.member_after_mutation.append(i[0:24] + '1')
                else:
                    self.member_after_mutation.append(i[0:24] + '0')
            else:
                self.member_after_mutation.append(i)

mutation = GeneMutation(os1.lista_osobnikow_po_selekcji,0.3)

mutation.edge_mutation()

print(len(mutation.member_after_mutation))

#print(mutation.member_after_mutation)
