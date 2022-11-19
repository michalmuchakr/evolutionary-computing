from Calculation import Calculation
from crorrsing import OnePointCrossing
from functions.goldstein_price import goldstein_price
from selection import RouletteSelection

USER_SELECTION = 'RouletteSelection'
USER_CROSSING = 'OnePoint'
EPOCH_AMOUNT = 10
POPULATION_SIZE = 10
ELITE_PERCENTAGE = 20
LIMIT = [-2, 2]
BEST_MEMBERS_SELECTION_PERCENTAGE = 3
TOURNAMENT_SELECTION_GROUP_SIZE = 2
MAXIMIZATION = False

selection_dictionary = {
  "RouletteSelection": RouletteSelection(),
}

crossing_dictionary = {
    "OnePoint": OnePointCrossing()
}

if __name__ == "__main__":
    calculation = Calculation(
        EPOCH_AMOUNT,
        POPULATION_SIZE,
        LIMIT[0],
        LIMIT[1],
        ELITE_PERCENTAGE,
        BEST_MEMBERS_SELECTION_PERCENTAGE,
        TOURNAMENT_SELECTION_GROUP_SIZE,
        selection_dictionary[USER_SELECTION],
        crossing_dictionary[USER_CROSSING],
        goldstein_price,
    )
    calculation.trigger()
