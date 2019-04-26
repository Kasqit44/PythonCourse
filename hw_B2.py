with open('rosalind_revc.txt', 'r') as file:
    dna = file.read()
def dna_transcript(dna):
    dna = dna[::-1]
    dna1=list(dna)
    for i in range(len(dna1)):
        if dna1[i] == 'A':
            dna1[i]='T'
        elif dna[i] =='T':
            dna1[i]='A'
        elif dna1[i]=='G':
            dna1[i]='C'
        elif dna1[i]=='C':
            dna1[i]='G'
    dna2= ''.join(dna1)
    print (dna2)
dna_transcript(dna)
