i = 0
while i<5:
    print("YES " + str(i))
    i = i + 1

print("Ho gaya!!")

i = int(input("Enter number : "))
while i<50:
    print(str(i))
    i = i + 1

fruits = ['banana', 'mango']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i + 1

fruits = ['banana', 'mango']
for item in fruits:
    print(item)

for i in range(1,8,2):
    print(i)

for i in range(10):
    print(i)
    if i == 5:
        break

for i in range(10):
    if i == 5:
        continue
    print(i)
