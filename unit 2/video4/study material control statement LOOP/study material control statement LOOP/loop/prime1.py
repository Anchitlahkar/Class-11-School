#check prime number
count=0
num=int(input('Enter a number'))
for i in range (1,num+1):
    if(num%i==0):
        count=count+1
if(count==2):
    print(num,'is prime')
else:
    print(num,'is not prime')
        
