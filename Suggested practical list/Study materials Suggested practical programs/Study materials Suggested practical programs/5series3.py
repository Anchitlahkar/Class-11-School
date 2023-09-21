#Series 1-x-x2-x3-x4-.............xn
n=int(input('Enter limit'))
x=int(input('Enter a number'))
res=1
for i in range(n):
    res-=x**i
print('Series sum is=',res)
