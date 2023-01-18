def is_armstrong_number(number):
    string = str(number)
    sum = 0
    for n in string:
        sum +=  int(n)**len(string)

    if sum == number:
        return True

    return False