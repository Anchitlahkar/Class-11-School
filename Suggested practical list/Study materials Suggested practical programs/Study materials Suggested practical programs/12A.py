# find smallest and largest element in and tuple
tup=(10,23,65,1,3,4,9)
lar=max(tup)
sm=min(tup)
print('largest-',lar)
print('smallest-',sm)

#without using max,min function
tup=(10,23,65,1,3,4,9)
l=tup[0]
s=tup[0]
for i in tup:
    if i >=l:
        l=i
    if i<=s:
        s=i
print('largest=',l)
print('smallest=',s)
