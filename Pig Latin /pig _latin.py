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

    # testing if the first character of the text is a vowel or not
    if text[0] not in vowels:
        cons = ''
        index = 0

        if 'y' in text:
            if len(text) == 2 and text[1] == 'y':
                return text[1] + text[0] + 'may'

            if text[0] != 'y' and text[-1] != 'y':
                return text[text.index('y'):] + text[:text.index('y')] + 'may'

            if text[0] == 'y' or text[-1]:
                return text + 'ay'

        for i in range(len(text)):
            if text[i] not in vowels:
                cons += text[i]
                idnex = i
            else:
                break

        output = text[i:] + cons + 'ay'
        return output

