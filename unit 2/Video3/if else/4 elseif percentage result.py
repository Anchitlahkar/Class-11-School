pc=int(input('Enter percentage'))
if pc>100:
    print('Wrong input....Enter less value')
elif (pc>=80):
    print("stand")
elif pc>=60:
    print('1st div')
elif pc>=45:
    print('2nd div')
else:
    print('fail')
