#example 1 
#just checking of number is even or odd, with if, elif, else statements 
a = float(input("enter a : "))
if(a%2==0):
    print("it is even number")
else:
    print("its a odd number")

#example 2
#compare the numbers
b = float(input("Enter b "))
c = float(input("Enter c "))
if(b>c):
    print("b is greater")
elif(b<c):
    print("b is lesser")
else:
    print("b == c")

#example 3
#to check if he/she can vote or not
d = int(input("LALLA enter your age : "))
if(d>=18):
    print("yeah , you can vote!!")
else:
    print("Nah, you can't vote!!")
