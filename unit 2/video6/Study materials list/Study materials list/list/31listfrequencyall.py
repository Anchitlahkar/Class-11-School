print("program to find the frequency of a given number")
l=[2,4,2,5,5,4,2,4,2,4,6,7,3,6]
le=len(l)
unique=[]
for i in range(le):
    if l[i] not in unique:
        unique.append(l[i])   
lee=len(unique)
print(l)
print("print unique")
print(unique)
for i in range (lee):
    count=0
    for j in range(le):
        if unique[i]==l[j]:
            count+=1
    print(unique[i],"has frequency",count,"in the list")
        
