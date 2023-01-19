def score(x, y):
    point = x + y
    if point < 0:
        point *= -1

    if point > 10:
        return 0
    elif point > 5:
        return 1
    elif point > 1:
        return 5
    else:
        return 10

