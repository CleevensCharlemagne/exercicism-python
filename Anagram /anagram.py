def find_anagrams(word, candidates):
    anagram = set()
    str = word.lower()
    arr = candidates

    for candidate in arr:
        okay = True

        if candidate.lower() != str:
            for car in candidate.lower():
                if (car in str) and (str.count(car) == candidate.lower().count(car)):
                    continue
                else:
                        okay = False
                        break
        if okay:
            anagram.add(candidate)

    return list(anagram)


candidates = ["Eons", "ONES"]
expected = ["Eons", "ONES"]
print(find_anagrams("nose", candidates))
