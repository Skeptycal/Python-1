import math

print "Use this to complete the square of a quadratic"

a = int(raw_input("a = "))
b = int(raw_input("b = "))
c = int(raw_input("c = "))

#(x+ (1/2)(b))^2 Left Side

x_squaredside = b/2

#Right Side
c_subtwo = c * (-1)
right_side = c_subtwo + (x_squaredside ** 2)
right_side = math.pow(right_side, 0.5)
x = right_side - x_squaredside

print x
