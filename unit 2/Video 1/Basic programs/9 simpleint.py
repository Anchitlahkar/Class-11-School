#Q. Write a program to input principal amount,time period, rate and calculate simple interest
#princi=int(input("enter princi"))
#time=int(input("enter princi"))
#rate=int(input("enter princi"))
#si=float((princi*time*rate)/100)
#print("simple int is:",si)



def simple(p,r,t):
    si=(p*r*t)/100
    print("simple interest is:",si)
princi=int(input("enter princi"))
time=int(input("enter time"))
rate=int(input("enter rate"))
simple(princi,rate,time)
