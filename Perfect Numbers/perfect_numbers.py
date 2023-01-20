# This function computes the factor of the argument passed
def n_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        factors = n_factors(number)
        if number > factors:
            return None
        elif number < factors:
            return None
        else:
            return None

