#SIMPLE STAR QUESTION
star = int(input("Enter number "))
n = int(input("Enter N "))
for i in range(star):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1),)