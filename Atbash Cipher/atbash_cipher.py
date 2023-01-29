def encode(plain_text):
    cipher = 'zyxwvutsrqponmlkjihgfedcba'


def decode(ciphered_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'zyxwvutsrqponmlkjihgfedcba'
    output = ''

    for l in ciphered_text:
        l = l.lower()
        if l in plain:
            output += plain[cipher.index(l)]
        el

    return output
