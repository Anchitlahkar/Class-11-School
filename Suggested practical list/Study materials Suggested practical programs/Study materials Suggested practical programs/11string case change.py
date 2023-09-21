#program to change case in string
st=input('Enter a string')
newst=[]
print('original string-',st)
for i in st:
    if i.isupper():
        newst.append(i.lower())
    elif i.islower():
        newst.append(i.upper())
print('After case change-',newst)
        
