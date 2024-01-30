def to_rna(dna_strand):
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna_strand = ''
    for dna in dna_strand:
        rna_strand += dna_to_rna[dna]
    return rna_strand
