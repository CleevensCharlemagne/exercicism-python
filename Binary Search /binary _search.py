def find(search_list, value):
    if value not in list:
        raise ValueError("value not in array")
    else:
        return search_list.index(value)