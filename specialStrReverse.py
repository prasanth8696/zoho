''' reverse the given string without change the special character if any occur

ex a#x&   op: x#a&

'''


b = input('enter ')
a = []
for i in b :
 a.append(i)
i = 0
j = len(a) -1

while(i<j) :

 if a[i].isalpha() == False :
   i = i+1
 if a[j].isalpha() == False :
   j = j - 1
 if a[i].isalpha()  == True and a[j].isalpha() == True :
   a[i],a[j] = a[j],a[i]
   i = i + 1
   j = j - 1


print(a)
temp = ''
for i in a :
  temp +=  i
print(temp)
