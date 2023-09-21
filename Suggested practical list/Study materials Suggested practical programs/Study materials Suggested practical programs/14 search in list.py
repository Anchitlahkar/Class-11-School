#input list/tuple and search element
lst=[6,7,8,9,5]
print('list elements are-',lst)

item=int(input('Enter element to be search'))
for i in range(0,len(lst)):
    if item == lst[i]:
        print(item,'is in index',i,'of the list')
        break
else:
    print(item,'not there in the list')
