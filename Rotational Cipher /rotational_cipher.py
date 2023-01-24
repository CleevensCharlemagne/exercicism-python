def rotate(text, key):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = text[key:] + text[:key]
    output = ''

    for n in text:
        output += cipher[plain.index(n)]

    return output

print()