st = input('Введите строку, и я определю длину самого короткого слова в ней ')
dd={}

for word in st.split():
    i = len(word)
    dd[word]=i
    
a = sorted(dd.values())[:1]
print (a[0])
