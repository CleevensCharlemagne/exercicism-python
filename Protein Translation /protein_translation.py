def proteins(strand):
    proteins = list()
    match = {'AUG':'Methionine', 'UUU':'Phenylalanine', 'UUC':'Phenylalanine',
             'UUA':'Leucine', 'UUG':'Leucine', 'UCU':'Serine', 'UCC':'Serine',
             'UCA':'Serine', 'UCG':'Serine', 'UAU':'Tyrosine', 'UAC':'Tyrosine',
             'UGU':'Cysteine', 'UGC':'Cysteine', 'UGG':'Tryptophan', 'UAA':'STOP',
             'UAG':'STOP', 'UGA':'STOP'}

    for i in range(len(strand) + 1):
        if i % 3 == 0 and i != 0:
            proteins.append(strand[i-3:i])

    print(proteins)

proteins("AUGUUUUCUUAAAUG")
