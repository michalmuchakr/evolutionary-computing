import random

class Osobnik_po_selekcji:
    lista_osobnikow_po_selekcji = []
    def __init__(self,lp,reprezentacja_binarna,przeliczenie,fitness_function):
        self.lp = lp
        self.reprezentacja_binarna = reprezentacja_binarna
        self.przeliczenie = przeliczenie
        self.fitness_function = fitness_function

    def rand_key(self,p):
        key1 = ""
        for i in range(p):
            temp = str(random.randint(0, 1))
            key1 += temp

        return (key1)

    def wygeneruj_liste_nowych_po_selekcji(self,range_start,range_stop):
        for x in range(range_start, range_stop):
            self.lista_osobnikow_po_selekcji.append(Osobnik_po_selekcji(x, self.rand_key(25),'xd','xdd'))

        return self.lista_osobnikow_po_selekcji

nowy_osobnik = Osobnik_po_selekcji(0,1111,'sdfadf','dfasdfas')
nowy_osobnik.wygeneruj_liste_nowych_po_selekcji(0,10)



class CrossingGens:

    member_after_crossing_one_point = []

    def __init__(self,list_of_object_gens):
        self.list_of_object_gens = list_of_object_gens
        self.list_of_individuals_after_selection = []

        for x in list_of_object_gens:
            self.list_of_individuals_after_selection.append(x.reprezentacja_binarna)

    def one_point_crossing(self,place_of_crossing,binary_value_for_the_draw_of_one,binary_value_for_the_draw_of_second):


            new_binary_value_for_the_draw_of_one = binary_value_for_the_draw_of_one[
                                                  0:place_of_crossing] + binary_value_for_the_draw_of_second[
                                                                           place_of_crossing:26]
            new_binary_value_for_the_draw_of_second = binary_value_for_the_draw_of_second[
                                                  0:place_of_crossing] + binary_value_for_the_draw_of_one[
                                                                           place_of_crossing:26]

            self.member_after_crossing_one_point.append(new_binary_value_for_the_draw_of_one)
            self.member_after_crossing_one_point.append(new_binary_value_for_the_draw_of_second)

    def two_point_crossing(self,first_half_of_the_crossing_site,second_half_of_the_crossing_site,binary_value_for_the_draw_of_one,binary_value_for_the_draw_of_second):
        new_binary_value_for_the_draw_of_one = binary_value_for_the_draw_of_one[
                                                0:first_half_of_the_crossing_site] + binary_value_for_the_draw_of_second[
                                                                         first_half_of_the_crossing_site:second_half_of_the_crossing_site] + binary_value_for_the_draw_of_one[second_half_of_the_crossing_site:26]

        new_binary_value_for_the_draw_of_second = binary_value_for_the_draw_of_second[
                                                  0:first_half_of_the_crossing_site] + binary_value_for_the_draw_of_one[
                                                                           first_half_of_the_crossing_site:second_half_of_the_crossing_site] + binary_value_for_the_draw_of_second[second_half_of_the_crossing_site:26]

        self.member_after_crossing_one_point.append(new_binary_value_for_the_draw_of_one)
        self.member_after_crossing_one_point.append(new_binary_value_for_the_draw_of_second)

    def three_point_crossing(self,first_half_of_the_crossing_site_three_point,second_half_of_the_crossing_site_three_point,third_half_of_the_crossing_site_three_point,binary_value_for_the_draw_of_one,binary_value_for_the_draw_of_second):
        new_binary_value_for_the_draw_of_one = binary_value_for_the_draw_of_one[
                                                0:first_half_of_the_crossing_site_three_point] + binary_value_for_the_draw_of_second[
                                                                         first_half_of_the_crossing_site_three_point:second_half_of_the_crossing_site_three_point] + binary_value_for_the_draw_of_one[second_half_of_the_crossing_site_three_point:third_half_of_the_crossing_site_three_point] + binary_value_for_the_draw_of_second[third_half_of_the_crossing_site_three_point:26]


        new_binary_value_for_the_draw_of_second = binary_value_for_the_draw_of_second[
                                                  0:first_half_of_the_crossing_site_three_point] + binary_value_for_the_draw_of_one[
                                                                                                   first_half_of_the_crossing_site_three_point:second_half_of_the_crossing_site_three_point] + binary_value_for_the_draw_of_second[second_half_of_the_crossing_site_three_point:third_half_of_the_crossing_site_three_point] + binary_value_for_the_draw_of_one[third_half_of_the_crossing_site_three_point:26]


        self.member_after_crossing_one_point.append(new_binary_value_for_the_draw_of_one)
        self.member_after_crossing_one_point.append(new_binary_value_for_the_draw_of_second)


    def call_crossover_functions(self, probability,which_function):
        while (len(self.member_after_crossing_one_point) != len(self.list_of_individuals_after_selection)):

            # losuje 2 osobnikow do krzyzowania
            first_draw = random.randint(0, len(self.list_of_individuals_after_selection) - 1)
            second_draw = random.randint(0, len(self.list_of_individuals_after_selection) - 1)

            while (first_draw == second_draw):
                second_draw = random.randint(0, len(self.list_of_individuals_after_selection))

            crossover_probability = random.uniform(0, 1)
            if crossover_probability < probability:
                # print('we will be able to cross', crossover_probability)
                # we draw the place of crossing, i.e. a number from 1 to 25
                #for one
                place_of_crossing = random.randint(1, 25)
                #for two
                first_half_of_the_crossing_site = random.randint(1, 11)
                second_half_of_the_crossing_site = random.randint(14, 25)
                #for three
                first_half_of_the_crossing_site_three_point = random.randint(1, 8)
                second_half_of_the_crossing_site_three_point = random.randint(9, 16)
                third_half_of_the_crossing_site_three_point = random.randint(17, 25)

                binary_value_for_the_draw_of_one = ''
                binary_value_for_the_draw_of_second = ''

                for x, obj in enumerate(self.list_of_individuals_after_selection):
                    if first_draw == x:
                        binary_value_for_the_draw_of_one = obj
                    elif second_draw == x:
                        binary_value_for_the_draw_of_second = obj



                if which_function == 1:
                    self.one_point_crossing(place_of_crossing,binary_value_for_the_draw_of_one,binary_value_for_the_draw_of_second)
                elif which_function == 2:
                    self.two_point_crossing(first_half_of_the_crossing_site,second_half_of_the_crossing_site,binary_value_for_the_draw_of_one,binary_value_for_the_draw_of_second)
                elif which_function == 3:
                    self.three_point_crossing(first_half_of_the_crossing_site_three_point,
                                         second_half_of_the_crossing_site_three_point,
                                         third_half_of_the_crossing_site_three_point, binary_value_for_the_draw_of_one,
                                         binary_value_for_the_draw_of_second)
                else:
                    break
            else:
                pass



crossing_gens_object = CrossingGens(nowy_osobnik.lista_osobnikow_po_selekcji)
#print(crossing_gens_object.list_of_individuals_after_selection)
crossing_gens_object.call_crossover_functions(0.8,4)
print(crossing_gens_object.member_after_crossing_one_point)


