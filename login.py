#creating a simple login interface 
username = input("Enter Your Name : ")
password = input("Enter Password : ")

print("Your Account Has Been Created Successfully!!")
print("Login Now!")

username2 = input("Enter Your Name : ")
password2 = input("ENter Your Password : ")

if username == username2 and password == password2:
    print("You Have Succefully Loged In!!")
else:
    print("Invalid credentials")
    
