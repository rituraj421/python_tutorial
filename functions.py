def unknown(stranger, age): #"def" is used to define function
    print("hello " +stranger+ ' u are ' +str(age)+ ' too old')

unknown('me',76)  

#we can define as many as functions we want to
def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/4)
    return p
marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1) #percentage1 = (sum(marks)/400)*100

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)
print(percentage1, percentage2)