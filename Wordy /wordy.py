def answer(question):
    words = question.split(" ")

    if words[0] == 'what' and words[1] == 'is':
        pass
    else:
        raise ValueError("syntax error")
