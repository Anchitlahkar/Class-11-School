l1=[1,2,3,12,32,1,4,76,87,79,68,91]
print("position 3 to -2 means from right side 3 to left side after -2")
seq=l1[3:-2]
print(seq)
print("position 4 to -4 means from right side 4 to left side after -4")
seq1=l1[4:-4]
print(seq1)
print("position 3 to 7 means from right side 3 to right side 7 numbers")
seq=l1[3:7]
print(seq)
print("position 5 to 9 means from right side 5 to right side 9 numbers")
seq=l1[5:9]
print(seq)
print("position 6 to 20 means from right side 6 to right side last no  numbers bcz 20 is not there")
seq=l1[6:20]
print(seq)

print("empty list will come 12: 20 range is not in this list")
seq=l1[12:20]
print(seq)
