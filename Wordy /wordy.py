def answer(question):
    words = question.split(" ")

    if '?' in words[-1]:
        words[-1] = words[-1][:-1]

    if words[0] == 'what' and words[1] == 'is':
        pass
    else:
        raise ValueError("syntax error")
