''' print the reciprocal of the given string

ex ab X    op : zy C

if any special char available  print the same  char here space is given
'''






a = input('enter ')
temp =''

for i in a :

 if i.isalpha():
   if i.isupper():
     dis = ord(i)  - 65
     temp += chr(90 - dis)
   else:
     dis = ord(i) - 97
     temp += chr(122 - dis)
 else :
   temp += i

print(temp)
