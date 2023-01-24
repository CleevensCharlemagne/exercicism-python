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


def length(list):
    pass


def map(function, list):
    pass


def foldl(function, list, initial):
    pass


def foldr(function, list, initial):
    pass


def reverse(list):
    pass
