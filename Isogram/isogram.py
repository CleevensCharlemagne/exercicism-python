def is_isogram(string):
    str1 = string.lower()
    for char in str1:
        if char.isalpha():
            if str1.count(char) > 1:
                return False
    return True

