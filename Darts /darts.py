def score(x, y):
    point = x + y
    if point < 0:
        point *= -1

    if point > 10 or point < 0:
        return 0
    elif point > 5 and point <= 10:
        return 1
    elif point >= 2 and point <= 5:
        return 5
    elif 1 <= point < 2 or x == y:
        return 10

