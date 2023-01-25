def translate(text):
    vowels = 'aeiou'
    output = ''

    if text[0] in vowels or text[:3] == 'xr' or text[:3] == 'yt':
        output = text + 'ay'

    return output
