# f = open('9.txt', 'r')
# data = f.read(5) #reads number of elements in provided file , if none then return whole file
# print(data)
# f.close()

f = open('another.txt', 'w')
f.write("Please write this to the file")
f.close()