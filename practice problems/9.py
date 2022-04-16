# Write a Python Program to Find the Area of a Rectangle Using Class, methods and
# constructor.


class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=float(input("Enter length of rectangle : "))
b=float(input("Enter breadth of rectangle : "))
obj=rectangle(a,b)
print("Area of rectangle is :",obj.area())
 
print()