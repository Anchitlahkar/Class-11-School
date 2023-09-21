'''Input a list of numbers and swap elements at the even location with the
elements at the odd location.'''

lst=list(input('Enter elements'))
print('Before swap',lst)
ln=len(lst)
print(ln)
for i in range(0,ln):
    if i%2==0:
        tmp=lst[i]
        lst[i]=lst[i+1]
        lst[i+1]=tmp
    i+=1
    
    
print('After swap',lst)
        
