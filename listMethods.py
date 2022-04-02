list1 = [1,3,4,5,6,7,]
list2 = ['apple', 'banana', 'mango']
list1.extend(list2) # "extend" command joins two lists 
print(list1)
list1.append(8) #"append" command adds item to the end of list
print(list1)
list1.insert(1,2) #"insert" command will insert 2 at the 1st index 
print(list1)
list1.remove(1) 
print(list1)
list1.clear() #"clear" command will delete all the date present in list1
print(list1)
print(list2.index('apple')) #gives index number of item


#given below are some more list commands 
'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list in ascending order

'''