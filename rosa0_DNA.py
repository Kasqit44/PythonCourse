with open('rosalind_dna.txt', 'r') as file:
    dna = file.read()
    
print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))