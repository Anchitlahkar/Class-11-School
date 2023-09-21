#write a program to check wether the string is a palindrome or not.
st1=input('Enter a sting')
l=len(st1)
p=l-1
index=0
while index<p:
    if st1[index]==st1[p]:
        index=index+1
        p=p-1
    else:
        print("String is not palindrome")
        break
else:
    print("String is a palindrome")



