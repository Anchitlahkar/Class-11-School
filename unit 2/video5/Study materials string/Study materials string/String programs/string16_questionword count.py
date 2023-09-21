#write a program that reads a line , then count words and display how many words are there in the line
line=input('Enter line')
x=line.split()
cnt=0
for i in x:
    cnt=cnt+1
print(cnt)
