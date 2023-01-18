def to_rna(dna_strand):
    DNA = "GCTA"
    RNA = "CGAU"

    if dna_strand == '':
        return ''

    output = ''
    for i in range(len(dna_strand)):
        index = DNA.index(dna_strand[i])
        output += RNA[index]

    return output

