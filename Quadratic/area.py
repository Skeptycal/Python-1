import math

def area():
    intro = raw_input("Select to determine the area of your shape: \n (1) Sqaure \n (2) Rectangle \n (3) Circle \n >>  ")
    print intro

    if  intro == "1":
        length = raw_input('Please enter the length of one side of the square')
        area = int(length) * int(length)
        print 'The area is %s' % (area)
    elif intro == "2":
        length = raw_input("Please enter a length of the Rectangle")
        width = raw_input("Please enter the width of the Rectangle")
        area = int(length) * int(width)
        print 'The area is %s' % (area)
    elif intro == "3":
        radius = raw_input("Please enter the radius of the circle")
        area = int(radius) * (math.pi) * int(radius)
        print 'The area is approximently %s' % (area)

    else:
        print "Sorry, that is not a choice"
        area()
area()
