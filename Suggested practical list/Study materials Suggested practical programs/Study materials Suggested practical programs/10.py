#Program to display and count vowel consonent lowercase uppercase in a string.
st=input('Enter a string')
lst=['a','e','i','o','u','A','E','I','O','U']  #lis of vowels
vls=[]  #defined to store vowels
cnst=[]  #defined to store consonent
upr=[] #defined to store uppercase characters
lwr=[] #defined to store lowercase characters
vc=0 #to store vowel count
cc=0 #to store consonent count
uc=0 #to store upercase characters count
lc=0 #to store lowercase characters count
for ch in st:
    if ch in lst:   #checking and counting vowel consonent
        vls.append(ch)
        vc+=1
    else:
        cnst.append(ch)
        cc+=1
    if ch.isupper():    #checking and counting uper lower
        upr.append(ch)  #adding upper list
        uc+=1
    else:
        lwr.append(ch)  #adding to lower list
        lc+=1
print('Vowel characters are -',vls)
print('Consonent characters are -',cnst)
print('uppercase characters-',upr)
print('lowercase characters-',lwr)
print('Number of vowels-',vc)
print('Number of consonents-',cc)
print('Number of upercase-',uc)
print('Number of lowercase-',lc)
        
