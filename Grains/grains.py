chess = []


def square(number):
    if number >= 1 and number <= 64:
        chess.append(1)
        i = 1
        while i < 64:
            chess.append(chess[i - 1] * 2)
            i += 1

    else:
        raise ValueError("square must be between 1 and 64")
    return chess[number - 1]


def total():
    sum = 0
    for grain in chess:
        sum += grain
    return sum
