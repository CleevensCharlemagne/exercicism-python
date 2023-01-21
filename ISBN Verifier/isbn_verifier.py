def is_valid(isbn):
    isbn_digits = list()
    test = 0
    is_valid = False

    # Add valid caracters to a list as integer
    for n in isbn:
        if n.isdigit():
            isbn_digits.append(int(n))
        elif n.isalpha():
            if n == 'X' and (isbn.index(n) == 0 or isbn.index(n) == len(isbn) - 1):
                isbn_digits.append(10)
            else:
                return False

    # check if the list has 10 caracters
    if len(isbn_digits) != 10:
        return False

    # Applying the given formula:
    # (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    b = 10
    for i in range(len(isbn_digits)):
        test += isbn_digits[i]*b
        b -= 1

    if test % 11 == 0:
        is_valid = True

    return is_valid
