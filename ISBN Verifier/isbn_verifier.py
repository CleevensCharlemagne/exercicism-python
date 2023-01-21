def is_valid(isbn):
    isbn_digits = list()
    test = 0
    is_valid = False

    for n in isbn:
        if n.isdigit():
            isbn_digits.append(int(n))
        elif n.isalpha():
            if n == 'X' and (isbn.index(n) == 0 or isbn.index(n) == len(isbn) -1):
                isbn_digits.append(10)
            else:
                return False

    if len(isbn_digits) != 10:
        return False

    b = 10
    for i in range(len(isbn_digits)):
        test += isbn_digits[i]*b
        b -= 1

    if test % 11 == 0:
        is_valid = True

    return is_valid
