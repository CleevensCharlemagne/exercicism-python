def sum_of_multiples(limit, multiples):
    l = set()
    for n in multiples:
        for i in range(limit):
            if i > 0:
                if i % n == 0:
                    l.add(i)
    return l


print(sum_of_multiples(10, [3, 5]))