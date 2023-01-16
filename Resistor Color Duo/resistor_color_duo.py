def color_code(color):
    colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    return colors.index(color)


def value(colors):
    output = ''

    for color in colors:
        output += str(color_code(color))

    if len(output) > 2:
        output = output[:2]

    return int(output)

