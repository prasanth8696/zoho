str = input('enter ')

a = []
count_dict = {}

for i in str :
 a.append(i)

for i in a :
  count = 0
  for j in a :
   if i == j :
    count = count + 1
    count_dict[i] = count

sum = 0
for i,j in count_dict.items() :
  sum = sum +  (ord(i)-96) * j


print(count_dict)
print (sum)
