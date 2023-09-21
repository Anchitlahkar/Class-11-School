l1=[2,4,1,5,7,54,9,12,32,42,36,17,90]
print("start:stop:step")
seq=l1[2:7:2]
print(seq)

print("start:stop:step")
seq=l1[4:10:3]
print(seq)


print("no start no stop step is 3")
seq=l1[::3]
print(seq)


print("reverse list no start no stop step is -1")
seq=l1[::-1]
print(seq)
