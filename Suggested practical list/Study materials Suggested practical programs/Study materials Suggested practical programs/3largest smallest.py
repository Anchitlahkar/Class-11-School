#Input three numbers and display the largest / smallest number.
a=int(input('Enter a number'))
b=int(input('Enter another number'))
c=int(input('Enter one more number'))
if a>b:
    if a>c:
        print(a,'is the largest one')
    else:
        print(c,'is the largest one')
        
else:
    if b>c:
        print(b,'is the largest one')
    else:
        print(c,'is the largest one')
