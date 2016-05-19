# -*- coding: utf-8 -*-
"""
Reverse Complementing a Strand of DNA
"""
def compliment_dna(d):
    compliment={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    rev=[compliment[i] for i in d]
    return rev
    
dna=input(' Enter the nucleotide sequence ')
dna=dna.upper();
rev_dna=''.join(compliment_dna(dna))
print(rev_dna[::-1])