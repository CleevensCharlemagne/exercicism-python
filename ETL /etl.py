def transform(legacy_data):
    tab = []
    for v in legacy_data.values():
        tab.append(v)
    print(tab)
transform({1: ["A", "E", "I", "O", "U"]})