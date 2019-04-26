with open('rosalind_subs.txt', 'r') as file: 
    dna = file.read() 
a = dna.splitlines() 
s1 = a[0] 
s2 = a[1]

def zest(s1, s2):
    n = len(s1)
    
    a = s1.find(s2)
    b= a+1
    print (b) #b нужно потому что по условию индексация должна быть с 1, а не с 0
    
    while a<=n:
        
        a = s1.find(s2, a+1, n+1)
        b = a+1
        if a != -1:
            
            print (b)
        else:
            break
zest(s1,s2)
