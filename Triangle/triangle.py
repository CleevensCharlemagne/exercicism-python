#Equilateral
def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if isTriangle(a, b, c):
        if a == b and a == c:
            return True

    return False

#Isosceles
def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if isTriangle(a, b, c):
        if a == b or a == c or b == c:
            return True

    return False

#Scalene
def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if isTriangle(a, b, c):
        if a != b and a != c and b != c:
            return True

    return False

#Verify if the given array is a valid triangle
def isTriangle(a, b, c):
    if a + b + c == 0:
        return False

    if a + b >= c and b + c >= a and a + c >= b:
        return True

    return False