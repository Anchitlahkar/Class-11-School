#uniform()-returns random floating point number,
#choice()- random selection from a sequence like a list,
#shuffle()- used to suffle or swap contents of a list'''
import random
print("uniform Lottery number(1,1000):",random.uniform(1,1000))

# 'choice()'
dchoice=random.choice(['1:East','2:west','3:North','4:south'])
print('My Direction is:',dchoice)


#'shuffle()')
a=['des','ses','mes','desf','apple']
print(random.shuffle(a))

random.shuffle(a)
print('resuffled:',a)


