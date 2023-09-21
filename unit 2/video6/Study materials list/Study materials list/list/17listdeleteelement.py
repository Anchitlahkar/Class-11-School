print("list delete elements")
l=[1,2,3,5,6,7,54,65,76,87,98]
del l[3]
print(l)

print("delete list slice")
del l[1:3]
print(l)

print("can delete only single element using pop no in slice")
l.pop(5)
print(l)

print("last item")
l.pop()
print(l)

print("first item")
l.pop(0)
print(l)

print("third item")
l.pop(2)
print(l)
