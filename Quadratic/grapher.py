from matplotlib import pyplot as plt
import numpy

print "This will find the rational roots of an equation"

a = int(raw_input("a => "))
b = int(raw_input("b => "))
c = int(raw_input("c => "))

p_q = str(c/a)

#local extremas
#0 = a*(x ** 2) + b*x + c

right = (((-1) * c) + ((0.5 * b) ** 2))
right_rooted = right ** 0.5

if right_rooted < 0:
    print "No real soultions"
else:
    left = (0.5) * b
    roots_pos = right_rooted - left
    roots_neg = (-1 * right_rooted) - left

    print "Roots ==> " + str(roots_pos) + ", " + str(roots_neg)

aa = str(a)
bb = str(b)
cc = str(c)

#equation
if a == 1:
    print ("x^2 + " + bb + "x + " + cc + " = y" )

else:
    print ("" + aa + "x^2 + " + bb + "x + " + cc + " = y" )

#Table
print "Table values"
minimum = int(raw_input("    min: "))
maximum = int(raw_input("    max: "))

print "---------------------"
print "| x-value | y-value |"

for i in range (minimum, (maximum + 1)):
    x_value = int(i)
    value_y = a*(i ** 2) + b*i + c

    print "     " + str(x_value) + "        " + str(value_y) + "     "


#Graph
x = numpy.linspace(-100, 100, 10000)

y = a*(x ** 2) + b*x + c

fig, ax = plt.subplots()
ax.plot(x,y)

plt.annotate('local min', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

prompt = raw_input("Show graph for the equation?")
if (prompt.lower() == "yes"):
    plt.show()
