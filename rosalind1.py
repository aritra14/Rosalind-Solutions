# Counting DNA Nucleotides

dna=input(' Enter the nucleotide sequence ')
dna=dna.upper();
acount=dna.count('A',0,len(dna));
tcount=dna.count('T',0,len(dna));
gcount=dna.count('G',0,len(dna));
ccount=dna.count('C',0,len(dna));
X=[acount,ccount,gcount,tcount];
print (' '.join(str(x) for x in X))
