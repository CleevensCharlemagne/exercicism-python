import re


def response(hey_bob):
    # remove mulitple spaces
    if hey_bob == "" or hey_bob.isspace():
        return 'Fine. Be that way!'

    hey_bob = re.sub(' +', ' ', hey_bob)
    if hey_bob[-1] == ' ':
        hey_bob = hey_bob[:-1]
    if hey_bob[-1] == '?' and hey_bob.isupper() == False:
        return 'Sure.'
    elif hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
