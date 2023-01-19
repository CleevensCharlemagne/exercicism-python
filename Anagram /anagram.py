def find_anagrams(word, candidates):
    anagram = set()

    for candidate in candidates:
        okay = True

        if candidate != word:
            for car in candidate:
                if (car in word) and (word.count(car) == candidate.count(car)):
                    continue
                else:
                        okay = False
                        break
        if okay:
            anagram.add(candidate)

    return list(anagram)


candidates = ["enlists", "google", "inlets", "banana"]
expected = ["inlets"]

print(find_anagrams("listen", candidates))
