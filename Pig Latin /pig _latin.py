def translate(text):
    vowels = 'aeiou'
    output = ''

    if text[0] in vowels or text[:3] == 'xr' or text[:3] == 'yt':
        output = text + 'ay'
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

        output = text[i+1:] + cons + 'ay'
        return output



