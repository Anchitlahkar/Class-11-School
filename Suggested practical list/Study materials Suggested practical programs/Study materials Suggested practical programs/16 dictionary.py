'''Create a dictionary with the roll number, name and marks of n students in a
class and display the names of students who have marks above 75.'''

number = int(input("Please enter the Maximum Number : "))
student = {}

for x in range(1, number + 1):
    name=input('Enter name')
    roll=int(input('roll no'))
    mark=int(input('Enter Mark'))
    student[name] = {'rollno':roll,'marks':mark}
    
for key in student:
    if student[key]['marks']>75:
        print ("student",key,':')
        print ('rollno=',str(student[key]['rollno']))
        print ('marks=',str(student[key]['marks']))
