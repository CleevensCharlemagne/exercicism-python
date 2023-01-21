def is_valid(isbn):
    isbn_digits = list()
    for n in isbn:
        if n.isdigit():
            isbn_digits.append(int(n))
        elif n == 'X':
            isbn_digits.append(10)

    return isbn_digits

print(is_valid("3-598-21508-8"))