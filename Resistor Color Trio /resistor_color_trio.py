def label(colors):
    colorsValue = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                   'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

    res = f'{str(colorsValue[colors[0]])}{str(colorsValue[colors[1]])}'
    if colorsValue[colors[2]] > 0:
        res += '0'*colorsValue[colors[2]]

    if len(res) > 3:
        res = str(int(int(res) / 1000)) + ' kiloohms'
    return res

print(label(["red", "black", "red"]))
