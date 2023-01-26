def translate(text):
    vowels = 'aeiou'
    output = ''

    # test if word starts by a vowel or xr or yt
    if text[0] in vowels or text[:3] == 'xr' or text[:3] == 'yt':
        output = text + 'ay'
        return output

    # test if text starts by qu
    if text[:2] == 'qu':
        output = text[2:] + 'quay'
        return output

    # test if text has only one consonant befor qu
    elif text[1:3] == 'qu':
        output = text[3:] + 'squay'
        return output

    # testing
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




