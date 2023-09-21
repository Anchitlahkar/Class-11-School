#prime numbers between range
def xc():
    num1=int(input("enter a number")) 
    num2=int(input("enter a number")) 
    for i in range(num1,num2):
        c=0  
        for j in range(1,i+1):
            if i%j==0:
                c+=1
            
        if c==2:
            print(i,"is prime")
        
        
xc()
