import math
a = int(input("Enter the 1st side length of triangle :"))
b = int(input("Enter the 2nd side length of triangle :"))
c = int(input("Enter the 3rd side length of the triangle :"))
s = (a + b + c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))


print(f"the area of the triangle is {area}")
