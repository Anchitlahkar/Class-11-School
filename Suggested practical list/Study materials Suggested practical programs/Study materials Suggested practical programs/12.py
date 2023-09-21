# find smallest and largest element in and list
lst=[10,23,65,1,3,4,9]
lar=max(lst)
sm=min(lst)
print('largest-',lar)
print('smallest-',sm)

#without using max,min function
lst=[10,23,65,1,3,4,9]
l=lst[0]
s=lst[0]
for i in lst:
    if i >=l:
        l=i
    if i<=s:
        s=i
print('largest=',l)
print('smallest=',s)

