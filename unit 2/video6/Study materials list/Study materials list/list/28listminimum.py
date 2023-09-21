l=list(input("enter list values"))
print("list elements are:",l)
le=len(l)
sm =l[0]
for i in range (le):
    if l[i]<sm:
        sm=l[i]
        po=i
print("smallet list element is:",sm)
print("And its index is:",po)



print("\nAnother way:\n")
l=[4,5,3,1,6,22,69]
le=len(l)
n=0
for i in range (le):
    if l[i]<l[n]:
        n=i
print("smallest",l[n])
print("index is:",l.index(l[n]))
