def steps(number):
    n_steps = 0
    n = number
    if (n <= 0):
        raise ValueError('Only positive integers are allowed')

    while (n > 1):
        if (n % 2 == 0):
            n = n / 2
            n_steps += 1
            print(n)
        else:
            n = (3 * n) + 1
            n_steps += 1
            print(n)
    return (n_steps)

print(steps(7))