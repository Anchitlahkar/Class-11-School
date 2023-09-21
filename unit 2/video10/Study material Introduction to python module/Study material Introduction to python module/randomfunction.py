print('binary search using randint function')
from random import randint
def binsrc(lst,item):
    mid=len(lst)//2
    low=0
    high=len(lst)-1
    while lst[mid] !=item and low<=high:
        if item>lst[mid]:
            low=mid+1
        else:
            high=mid-1
        mid=(low+high)//2
    if low>high:
        return none
    else:
        return mid
a=[]
for i in range(10):
    a.append(randint(1,20))
a.sort()    #sort() used to arrange the  list element in ascending order
print(a)

value= int(input("enter item"))
print ("Element fund at the index:",binsrc(a,value))
