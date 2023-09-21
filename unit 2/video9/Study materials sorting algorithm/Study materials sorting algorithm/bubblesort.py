print ('program to sort a list using bubble sort')
bb=[5,6,1,8,9,2,4,3,10]
print ('original list',bb)
le=len(bb) 
for i in range(le):
    for j in range(0,le-1-1):
        if bb[j]>bb[j+1]:
            bb[j],bb[j+1]=bb[j+1],bb[j]
    print ('after pass',i,'element :',bb)
print ('list after sorting:\n')
print (bb)
