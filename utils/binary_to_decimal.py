def binary_to_decimal(binary, left_limit, right_limit):
    """
    Calculate decimal value of the binary array

    Attributes:
        binary: array of the True/False values
        left_limit: lower limit of the final value
        right_limit: upper limit of the final value
    """
    binary_string = ''.join(map(lambda value: '0' if value == False else '1', binary))
    length = len(binary)
    return left_limit + int(binary_string, 2) * (right_limit - left_limit) / (pow(2, length) - 1)
