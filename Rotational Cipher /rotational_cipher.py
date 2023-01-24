def rotate(text, key):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = plain[key:] + plain[:key]
    output = ''

    for n in text:
        if n in plain:
            output += cipher[plain.index(n)]
        else:
            output += n

    print(cipher)

    return output

print(rotate('The quick brown fox jumps over the lazy dog.', 13))