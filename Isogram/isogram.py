def is_isogram(string):
    str = string.lower()
    for char in str:
        if char.islapha() and str.count(char) > 1:
            return False
    return True

