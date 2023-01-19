def sum_of_multiples(limit, multiples):
    l = set()
    output = 0
    for n in multiples:
      if n == 0:
          break
      for i in range(limit):
        if i > 0:
          if i % n == 0:
            l.add(i)

    for el in l:
      output += el

    return output