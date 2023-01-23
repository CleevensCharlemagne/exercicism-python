def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if isTriangle(a, b, c):
        if a == b and a == c:
            return True

    return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if isTriangle(a, b, c):
        if a == b or a == c or b == c:
            return True

    return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if isTriangle(a, b, c):
        if a != b and a != c and b != c:
            return True

    return False


def isTriangle(a, b, c):
    if a < 1 or b < 1 or c < 1:
        return False

    if a + b >= c and b + c >= a and a + c >= b:
        return True

    return False