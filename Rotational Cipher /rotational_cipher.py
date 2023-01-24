def rotate(str, key):
    text = str.lower()
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = plain[key:] + plain[:key]
    output = ''

    for i in range(len(text)):
        if text[i] in plain:
            t = cipher[plain.index(text[i])]
            if str[i].isupper():
                t = t.upper()
            output += t

        else:
            output += text[i]

    print(cipher)

    return output

print(rotate('The quick brown fox jumps over the lazy dog.', 13))