def abbreviate(words):
    output = ''
    str = ''
    for n in words:
        if n == '-' or n == '_':
            str += ' '
        else:
            str += n

    arr = str.split()

    for n in arr:
        output += n[0].upper()

    return output
