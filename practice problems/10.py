# Write a Python Program to Create a Class and Compute the Area and the
# Perimeter of the Circle

import math # it imports all math modules 
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
 
a=float(input("Enter radius of circle : "))
obj=circle(a)
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),2))