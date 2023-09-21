import circle
import rectangle
choice=0
ch='y'
while (ch=='y'):
    print ('Menu')
    print ('1.Area of a circle')
    print ('2.Circumference of a circle')
    print ('3.Area of a rectangle')
    print ('4.Perimeter of a rectangle')
    print ('5.Quit')
    choice=int(input('Enter your choice'))
    if(choice==1):
        redius=int(input('Enter circle redius'))
        print ('The area is:',circle.circle_area(redius))
    elif(choice==2):
        redius=int(input('Enter circle redius'))
        print ('The circumference is:',circle.circumference(redius))
    elif(choice==3):
        width=int(input('Enter the width of the rectangle:'))
        length=int(input('Enter the length of the rectangle:'))
        print ('The area of rectangle is:',rectangle.rectangle_area(width,length))
    elif(choice==4):
        width=int(input('Enter the width of the rectangle:'))
        length=int(input('Enter the length of the rectangle:'))
        print ('The perimeter is:',rectangle.perimeter(width,length))
    elif(choice==5):
        print ('Exiting the program......')
    else:
        print('Error: invalid section')
