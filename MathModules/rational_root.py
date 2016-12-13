from matplotlib import pyplot as plt
import numpy

print "What is the equation you are trying to find all of the real rational roots for?"

a = int(raw_input("a ==>  "))
b = int(raw_input("b ==>  "))
c = int(raw_input("c ==>  "))
d = int(raw_input("d ==>  "))

d = d/a

if d >= 0:
    ran_neg = d - (2 * d)
    ran_pos = d
else:
    ran_pos = d - (2 * d)
    ran_neg = d

for i in range(ran_neg, ran_pos):
    eq = ((a*i) * (a*i) * (a * i)) + ((b*i) * (b*i)) + c*i + d
    if eq == 0:
        print ("A Rational Root is ==> " + str(i))

x = numpy.linspace(-10, 10, 1000)
y = a*(x ** 3) + b*(x ** 2) + c*x + d

fig, ax = plt.subplots()
ax.plot(x,y)

plt.show()
