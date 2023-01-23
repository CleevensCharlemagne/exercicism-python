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
    if a + b >= c or b + c >= a or a + c >= b:
        return True

    return False