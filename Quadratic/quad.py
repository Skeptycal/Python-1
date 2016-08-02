import math

def quad():

    print "This calculates a quadratic using the quadratic formula"
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))

    d = (b ** 2) - 4 * a * c
    if d < 0:
        print "The solutions are complex... sorry"

    positive_root = (- b + math.sqrt(d)) / 2 * a
    negative_root = (- b - math.sqrt(d)) / 2 * a
    print (positive_root, negative_root)

quad()
