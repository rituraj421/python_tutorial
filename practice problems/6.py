#dictionaries in python

#empty Dictionary
Dict = {}
print("This Is An Empty Dictionary: ")
print(Dict)

# Adding elements
Dict[0] = 'rituraj'
Dict[2] = 'roj'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") #\n for new line
print(Dict)

# Adding set of values
Dict['Value_set'] = 1, 2, 3
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[1] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
