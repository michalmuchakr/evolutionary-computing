from Calculation import Calculation
from functions.goldstein_price import goldstein_price
from selection import RouletteSelection

USER_SELECTION = 'RouletteSelection'
EPOCH_AMOUNT = 10
POPULATION_SIZE = 10
LIMIT = [-2, 2]
BEST_MEMBERS_SELECTION_PERCENTAGE = 3
TOURNAMENT_SELECTION_GROUP_SIZE = 2
MAXIMIZATION = False

selection_dictionary = {
  "RouletteSelection": RouletteSelection(),
}

crossing_dictionary = {
    "OnePoint": 1
}

if __name__ == "__main__":
    calculation = Calculation(
        EPOCH_AMOUNT,
        POPULATION_SIZE,
        LIMIT[0],
        LIMIT[1],
        BEST_MEMBERS_SELECTION_PERCENTAGE,
        TOURNAMENT_SELECTION_GROUP_SIZE,
        selection_dictionary[USER_SELECTION],
        goldstein_price
    )
    calculation.trigger()
