def reverse(text):
    output = ''
    i = len(text) - 1
    while i >= 0:
        output += text[i]
        i -= 1
    return output

