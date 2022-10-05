class Calculation:
    # Class that will trigger calculation
    def __init__(self, variable_one, variable_two):
        self.variableOne = variable_one
        self.variable_two = variable_two

    def add_variables(self):
        print(self.variableOne + self.variable_two)


calculationProject = Calculation(1, 2)
calculationProject.add_variables()
