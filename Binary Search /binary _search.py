def find(search_list, value):
    if value not in list:
        raise ValueError("value not in array")

    return search_list.index(value)
