import math

x1 = float(input("What is the x-coordinate of the first point:"))
y1 = float(input("What is the y-coordinate of the first point:"))
x2 = float(input("What is the x-coordinate of the second point:"))
y2 = float(input("What is the y-coordinate of the second point:"))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print("The distance between the two points is:", round(distance, 2))

#Reflection:
#I learned that in order to get an accurate calculation, i used the math library, because sqrt() and pow() do the calculations for me
#Without the math library, i would have to figure out the calculations myself, which is gonna be complicated
