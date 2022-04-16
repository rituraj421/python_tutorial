#Write a python program to that accepts length of three sides of a triangle as
#inputs

a = float(input("Enter side A : "))
b = float(input("Enter side B : "))
c = float(input("Enter side C : "))

if a + b > c and b + c > a and a + c > b :

    print("It's a Triangle")
else :
    print("It's not a triangle")

#to check if a tirangle is right angle or not
if(a**2 + b**2 == c**2):
    print("It's a right angled triangle")
else:
    print("It's not a right angled triangle")