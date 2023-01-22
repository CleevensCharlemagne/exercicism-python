def answer(question):
    words = question.split(" ")
    print(words)

    if '?' in words[-1]:
        words[-1] = words[-1][:-1]

    print(words)
    if words[0] == 'what' and words[1] == 'is':
        pass
    else:
        raise ValueError("syntax error")

answer("What is 5?")