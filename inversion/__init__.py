import random

def inversion(array, probability):
    """
    Attributes:
        array: array of any values
        probability: probability of inversion (float)
    """
    if random.random() > probability: return array

    start = random.randint(0, len(array) - 1)
    end = random.randint(start + 1, len(array))

    fragment = array[start:end][::-1]
    return array[0:start] + fragment + array[end:]
