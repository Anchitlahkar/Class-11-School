#Series 1+x+x2+x3+x4+.............xn
n=int(input('Enter limit'))
x=int(input('Enter a number'))
sum=0
for i in range(n):
    sum+=x**i
print('Series sum is=',sum)
