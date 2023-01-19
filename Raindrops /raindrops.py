def convert(number):
    pling = 'Pling'
    plang = 'Plang'
    plong = 'Plong'
    output = ''

    if number % 3 == 0:
        output = pling

    if number % 5 == 0:
        output += plang

    if number % 7 == 0:
        output += plong

    if len(output) == 0:
        output = str(number)

    return output
