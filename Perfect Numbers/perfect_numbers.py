def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        pass

# This function computes the factor of the argument passed
def print_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
