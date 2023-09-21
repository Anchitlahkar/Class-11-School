#Enter principal amount, time calculate simple interest considering following condition.
#principal >=2000 and time >= 5, rate =2
#principal >=2000 and time < 5, rate =3
#principal <2000 and time >= 5, rate =4
#principal <2000 and time < 5, rate =5


p=int(input('Entere principal amount'))
t=int (input('Enter time'))
if p>=2000:
    if t>=5:
        r=2
    else:
        r=3
else:
    if t>=5:
        r=4
    else:
        r=5
si=p*t*r/100
print('Simple interest=',si)
    
