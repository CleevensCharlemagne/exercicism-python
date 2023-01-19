def find_anagrams(word, candidates):
    anagram = set()

    for candidate in candidates:
        okay = True

        if candidate != word:
            for car in candidate:
                if car not in word:
                    okay = False
                    break
        anagram.add(candidate)

    return list(anagram)