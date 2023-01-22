def answer(question):
    words = question.split(" ")

    if '?' in words[-1]:
        words[-1] = words[-1][:-1]

    if words[0] == 'What' and words[1] == 'is':
        if len(words) == 3:
            if words[-1].isdigit():
                return int(words[-1])
    else:
        raise ValueError("syntax error")

print(answer("What is 5?"))