#prime numbers between range
def xc():
    num1=int(input("enter a number"))
    c=0
    for j in range(1,num1+1):
        if num1%j==0:
            c+=1
    if c==2:
        print(num1,"is prime")
    else:
        print(num1,"is not prime")    
xc()
