# This function computes the factor of the argument passed
def n_factors(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    print('factors:', factors)
    return factors

def sum_factors(factors):
    sum = 0
    for factor in factors:
        sum += factor
    print('sum_factors', sum)
    return sum

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        factors = n_factors(number)
        sumFactors = sum_factors(factors)
        if number > sumFactors:
            return 'abundant'
        elif number < sumFactors:
            return 'deficient'
        else:
            return 'perfect'

classify(6)

