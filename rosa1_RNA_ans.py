with open('rosalind_rna.txt', 'r') as file:
    rna = file.read()

rna = rna.upper().replace('T','U')
print (rna)
