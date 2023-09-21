#Write a program to remove vowels from a string
#str1=input('Enter String')  #Marias public school
str1="Marias Public School"
str2=""
for i in range(len(str1)):
    if str1[i] not in 'aeiouAEIOU':
        str2=str2+str1[i]
print("Original string is:",str1)
print("New string is:",str2)
