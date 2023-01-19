def transform(legacy_data):
    tab = []
    tab2 = []
    output = {}
    for v in legacy_data.values():
        tab.append(v)

    for t in tab:
        for e in t:
            tab2.append(e)

    tab2.sort()

    for t in tab2:
        for k in legacy_data.keys():
            if t in legacy_data[k]:
                output[t.lower()] = k
                break

    return output