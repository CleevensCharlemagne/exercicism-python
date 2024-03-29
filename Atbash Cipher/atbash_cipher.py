import string


def encode(plain_text):
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'zyxwvutsrqponmlkjihgfedcba'
    punc = string.punctuation

    plain_text = plain_text.lower()
    output = ''
    i = 0

    for l in plain_text:
        l = l.lower()
        if l in plain:
            output += plain[cipher.index(l)]
            i += 1
        elif l != ' ' and l not in punc:
            output += l
            i += 1

        if i == 5:
            output += ' '
            i = 0

    if output[-1] == ' ':
        output = output[:-1]

    return output
#Decode method
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
