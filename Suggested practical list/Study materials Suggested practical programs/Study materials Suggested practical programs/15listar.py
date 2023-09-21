#Input a list of numbers and test if a number is equal to the sum of the cubes of
#its digits.Find the smallest and largest such number from the given list of
#numbers.
lst=[407,153,39,871,25,370]
ams=[] # to store armstrong number

for i in range(0,len(lst)):
    sum=0
    temp=lst[i]
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if lst[i] == sum:
        ams.append(lst[i])
   
print("Armstrong numbers are in the list-",ams)
print ('Largest armstrong number is-',max(ams))
print ('smallest armstrong number is-',min(ams))
    


