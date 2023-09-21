print("program to find the frequency of a given number")
l=[2,4,2,5,5,4,2,4]
count=0
le=len(l)
item=int(input("enter a number"))
for i in range(le):
    if item==l[i]:
        count+=1
if count==0:
    print(item,"is not in list")
else:
    print(item,"has frequency as",count,"in the given list")

