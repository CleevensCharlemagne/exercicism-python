"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    output = ''
    arr = title.split(" ")
    for word in arr:
        output += word.capitalize() + " "
    output = output[:-1]

    return output


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """

    return (sentence[-1] == '.')


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    str = sentence

    while str[0] == ' ':
      str = str[1:]

    while str[-1] == ' ':
      str = str[:-2]

    return str


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    arr = []
    temp = ''
    if(check_sentence_ending(sentence)):
      sentence = sentence[:-1]
      temp = '.'

    arr = sentence.split(' ')

    output = ''
    for i in range(len(arr)):
        if arr[i] == old_word:
            output += new_word + ' '
        else:
          output += arr[i] + ' '

    output = output[:-1]+temp

    return output
