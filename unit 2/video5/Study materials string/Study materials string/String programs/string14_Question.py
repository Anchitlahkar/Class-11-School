#write a program to count the number of vowels
#in the string pineapple.
word='pineapple'
count=0
for letter in word:
    if letter in('a','e','i','o','u'):
        count=count+1
print(count)


#ans- 4
