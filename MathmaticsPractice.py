print "-----#1-----"
#Find the area of a circle with a known radius
import math
radius = float(input("Enter your radius: "))
area = 0.00
area = (math.pi)*(pow(radius,2))
print area

print "-----#2-----"
#Find the approximate value of .... where x and n are given
x = float(input("Enter your x: "))
n = float(input("Enter your n: "))
ans = 0.00
ans = pow((1+x),n)
print ans

print "-----#3-----"
#Find both roots of the quadratic equation where a,b, and c are known
a = float(input("Enter your a: "))
b = float(input("Enter your b: "))
c = float(input("Enter your c: "))
d = b**2-4*a*c # discriminant
if d < 0:
    print "NaN"
elif d == 0:
    root1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    print root1
else:
    root1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    root2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print root1, root2
