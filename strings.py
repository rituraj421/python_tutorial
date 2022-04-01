print('hey, \n hi how are you')
name = 'rituraj'
print(name[1]) # in python index starts from 0,
print(name.upper()) #makes all letters uppercase
print(name.lower()) #makes all the letters in lowercase
print(name.islower()) #checks whether the given string is in lower case, if yes then it returns true else false
print(name.isupper()) #chacks whether the given string is is in upper case , if yes prints true else false
print(name.upper().isupper()) # it will print true, as we converted the string into uppercase 
print(len(name)) #prints the length of the string
print(name.replace('i', 'a')) #replaces the character 
print(name.index('r')) # gives the index number of character ypu have entered, here it will print index, as 0, not 4