def is_pangram(sentence):
    # List of all the letters
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # Loop through the letters
    for letter in letters:
        #Check if the letter is in the sequence
        if letter not in sentence.lower():
            return False

    return True
