l=list(input("enter list values"))
print("list elements are:",l)
item=int(input("enter a number"))
le=len(l)
for i in range(0,le):
    if item==l[i]:
        print(item,"is found in the index",i+1)
        break
else:
    print(item,"is not found in the list")
        
    
