# num = 0 
# while num < 10:
#      num += 1 
#      if num == 6: 
#          pass  #also check with , replacing pass with continue & break
#      print(num)

num = 1 
odd_nums = [] 
while num: 
    if num % 2 != 0: 
        odd_nums.append(num)
    if num >=20: 
        break 
    num += 1 
    print("Odd numbers: ", odd_nums)