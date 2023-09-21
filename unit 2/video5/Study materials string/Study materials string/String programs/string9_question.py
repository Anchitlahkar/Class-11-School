#write a program to accept a string and return string having first
#letter of each word in capital letter
st=input("Enter a string")   
print("original string", st)
st1=""   
x=st.split()
for i in x:
    st1+=i.capitalize()+" "           
print(st1)








