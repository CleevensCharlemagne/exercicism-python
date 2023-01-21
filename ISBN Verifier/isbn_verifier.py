def is_valid(isbn):
    isbn_digits = list()
    test = 0
    is_valid = False
    for n in isbn:
        if n.isdigit():
            isbn_digits.append(int(n))
        elif n == 'X':
            isbn_digits.append(10)

    b = 10
    for i in range(len(isbn_digits)):
        test += isbn_digits[i]*b


    if test % 11 == 0:
        is_valid = True

    return is_valid

print(is_valid("3-598-21507-X"))