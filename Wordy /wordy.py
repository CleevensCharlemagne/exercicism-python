def answer(question):
    words = question.split(" ")
    digit = False

    #Removing the question mark
    if '?' in words[-1]:
        words[-1] = words[-1][:-1]

    for c in question:
        if c.isdigit():
            digit = True

    if digit == False:
        raise ValueError("unknown operation")
        return

    if not question[-1].isdigit():
        raise ValueError("syntax error")
        return


    #Checking the beginning of the question
    if words[0] == 'What' and words[1] == 'is':
        if len(words) == 3:
            if words[-1].isdigit():
                return int(words[-1])

        elif len(words) == 4:
            raise ValueError("unknown operation")

        elif len(words) < 3:
            raise ValueError("syntax error")



    else:
        raise ValueError("syntax error")

print(answer("What is 1 plus?"))