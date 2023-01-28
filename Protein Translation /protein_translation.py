def proteins(strand):
    match = {'AUG':'Methionine', 'UUU':'Phenylalanine', 'UUC':'Phenylalanine',
             'UUA':'Leucine', 'UUG':'Leucine', 'UCU':'Serine', 'UCC':'Serine',
             'UCA':'Serine', 'UCG':'Serine', 'UAU':'Tyrosine', 'UAC':'Tyrosine',
             'UGU':'Cysteine', 'UGC':'Cysteine', 'UGG':'Tryptophan', 'UAA':'STOP',
             'UAG':'STOP', 'UGA':'STOP'}

    for i in range(2 , len(strand), 3):
        print(strand[i-2:i])
