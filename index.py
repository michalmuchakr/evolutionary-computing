from Calculation import Calculation
from functions.goldstein_price import goldstein_price
from selection import RouletteSelection

EPOCH_AMOUNT = 10
POPULATION_SIZE = 10
LIMIT = [-2, 2]
BEST_MEMBERS_SELECTION_PERCENTAGE = 3
TOURNAMENT_SELECTION_GROUP_SIZE = 2

if __name__ == "__main__":
    calculation = Calculation(
        EPOCH_AMOUNT,
        POPULATION_SIZE,
        LIMIT[0],
        LIMIT[1],
        BEST_MEMBERS_SELECTION_PERCENTAGE,
        TOURNAMENT_SELECTION_GROUP_SIZE,
        RouletteSelection(),
        goldstein_price
    )
    calculation.trigger()
