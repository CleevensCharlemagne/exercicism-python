def rotate(text, key):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = plain[key:] + plain[:key]
    output = ''

    for i in range(len(text)):
        if text[i] in plain:
            output += cipher[plain.index(text[i])]
        else:
            output += text[i]

    print(cipher)

    return output

print(rotate('The quick brown fox jumps over the lazy dog.', 13))