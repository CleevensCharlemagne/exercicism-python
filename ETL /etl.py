def transform(legacy_data):
    tab = []
    tab2 = []
    for v in legacy_data.values():
        tab.append(v)
    print(tab)

    for t in tab:
      for e in t:
        tab2.append(e)

    tab2.sort()
    print(tab2)
transform({1: ["A", "E"], 2: ["D", "G"]})