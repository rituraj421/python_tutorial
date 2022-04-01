#PYTHON LISTS ARE MUTABLE , ORDERED SEQUENCE OF ELEMENTS.
list = ['raman', 'tokyo', False, 'dharavi', 1,'juinagar']
print(list)
print(len(list))
print(list[0]) #it will print 'raman' 
print(list[0][1]) #here it will print 1st(a) index of 0th(raman) element 
print(list[0:]) # it will print whole list 
print(type(list)) 
list[0] = 'raju' # it will replace index number 0(raman) with raju, as lists are mutable
print(list)
print(list[-1]) # it will print list from last to first ,due to negative sign

#alternate method
list1 = list(('ratu',True))
print(list1)