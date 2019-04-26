with open('rosalind_hamm.txt', 'r') as file: 
    dna = file.read() 
a = dna.splitlines() 
dna_1 = a[0] 
dna_2 = a[1] 

def dna_compare(dna_1, dna_2):
    dna_1=list(dna_1)
    dna_2=list(dna_2) 
    i = 0 
    for n1 in range(len(dna_1)):
         if dna_1[n1]!=dna_2[n1]:
             i += 1

    print (i)
        
dna_compare(dna_1, dna_2)
