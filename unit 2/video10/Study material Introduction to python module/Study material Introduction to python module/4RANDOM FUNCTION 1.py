#'''randint() - function accepts two parameters returns
#   a number between a and b
#   if ranint(0,5) it may return any number including 0 and 5''')
import random
print (random.randint(0,5))

#'Q. function to fills a list with numbers using randint()')
from random import randint
def fill_list(lst,limit,low,high):
    for i in range(limit):
        lst.append(randint(low,high))
minimum=int(input("min:"))
maximum=int(input("max:"))
n=int(input("number limit:"))
a=[]
fill_list(a,n,minimum,maximum)
print (a)
