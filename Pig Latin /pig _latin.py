def translate(text):
    vowels = 'aeiou'
    output = ''

    if text[0] in vowels or text[:3] == 'xr' or text[:3] == 'yt':
        output = text + 'ay'
        return output

    # if 'y' in text:
    #     if text[0] != 'y' and text[-1] != 'y':
    #         output = text[:text.index('y')] + "may"
    #         return output

    if text[:2] == 'qu':
        output = text[2:] + 'quay'
        return output

    elif text[1:3] == 'qu':
        output = text[3:] + 'squay'
        return output

    if text[0] not in vowels:
        cons = ''
        index = 0
        for i in range(len(text)):
            if text[i] not in vowels:
                cons += text[i]
                idnex = i
            else:
                break

        output = text[i:] + cons + 'ay'
        return output




