def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if isTriangle(a, b, c):
        if a == b and a == c:
            return True

    return False

def isosceles(sides):
    pass


def scalene(sides):
    pass

def isTriangle(a, b, c):
    if a + b >= c or b + c >= a or a + c >= b:
        return True

    return False