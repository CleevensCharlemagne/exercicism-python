def encode(plain_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'zyxwvutsrqponmlkjihgfedcba'

    plain_text = plain_text.lower()
    output = ''

    for l in plain_text:
        l = l.lower()
        if l in plain:
            output += plain[cipher.index(l)]
        elif l != ' ':
            output += l

        if len(output) == 5:
            output += ' '

    if output[-1] == ' ':
        output = output[:-1]

    return output

def decode(ciphered_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'zyxwvutsrqponmlkjihgfedcba'
    output = ''

    for l in ciphered_text:
        l = l.lower()
        if l in plain:
            output += plain[cipher.index(l)]
        elif l != ' ':
            output += l

    return output
