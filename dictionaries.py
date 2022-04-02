myDict = {
    "Fast": "In a quick manner",
    "ritu": "A coder",
    "marks": "1,3,6,",
    "anotherdict": {'ritu':'khiladi'},
}
print(myDict['Fast'])
print(myDict['ritu'])
print(myDict['marks'])
print(myDict['anotherdict']['ritu'])

print(myDict.keys()) #prints the keys of dictionary
print(myDict.values()) #prints the values pf dictionary
updateDict = {
    "Lovish": "Friend"
}
myDict.update(updateDict)
print(myDict)
print(myDict.get("ritu"))
print(myDict['ritu2']) #returns error , as it is not present
print(myDict.get("ritu2")) # returns none , 
a = {} #empty dictionary