def append(list1, list2):
    for l in list2:
        list1.append(l)

    return list1


def concat(lists):
    flatten = []

    if len(lists) == 0:
        return []

    for sub in lists:
        for li in sub:
            flatten.append(li)

    return flatten


def filter(function, lst):
    output = []

    if len(lst) == 0:
        return []

    for n in lst:
        if function(n):
            output.append(n)

    return output


def length(lst):
    count = 0

    if len(lst) == 0:
        return count

    for n in lst:
        count += 1

    return count


def map(function, lst):
    output = []
    if len(lst) == 0:
        return output

    for item in lst:
        output.append(function(item))

    return output


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass
