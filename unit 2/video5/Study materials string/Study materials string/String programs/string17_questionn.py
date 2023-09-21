#write a function vowcount() in python which takes a string as an argument
#the function should count and display the occurance of words starting with a vowel
#in the given string
#Example
#if the string content is as follows
#Updated information is simplified by official websites.
#The vowcount() function should display the output as
#Updated
#information
#is
#official
def vowcount():
    cnt=0
    str1=input("Enter a string")
    word=str1.split()
    for i in word:
        if i[0] in 'aeiou' or i[0] in 'AEIOU':
            cnt+=1
            print (i)
    print("vowelwords:",cnt)
vowcount()
