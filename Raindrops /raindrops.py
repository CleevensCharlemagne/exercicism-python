def convert(number):
    pling = 'Pling'
    plang = 'Plang'
    Plong = 'Plong'
    output = ''

    if number % 3 == 0:
        output = pling

    if number % 5 == 0:
        output += plang
