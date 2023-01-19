def score(x, y):
    point = sqrt(x ** 2 + y ** 2)

    if point > 10:
        return 0
    elif point > 5:
        return 1
    elif point > 1:
        return 5
    else:
        return 10

