# Python program to demonstrate  
# string concatenation  

#method 1
str1 = input("Enter str1 :")  
str2 = input("Enter str2 :")  
  
# % Operator is used here to combine the string  
print("% s % s" % (str1, str2))

#method 2
str1 = "Hello"  
str2 = "rituraj"  
    
print("{} {}".format(str1, str2))   
  
# store the result in another variable   
str3 = "{} {}".format(str1, str2)   
  
print(str3)

#method3
str1 = "Hii "  
str2 = "ratu"  
  
# + Operator is used to strings concatenation  
str3 = str1 + str2  
print(str3)   # Printing the new combined string