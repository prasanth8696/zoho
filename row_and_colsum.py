
m = int(input('enter row '))
n = int(input('enter column '))

a = []
for i in range(m) :
 c = []
 for j in range(n) :
  c.append(int(input('enter ')))
 a.append(c)

#print the matrix



list1 = []
sum1 = 0
sum2 = 0
list2 = []

for i in range(m) :

  for j in range(n) :

    sum1 = sum1 + a[i][j]
    sum2 = sum2 + a[j][i]

  list1.append(sum1)
  list2.append(sum2)
  sum1 = 0
  sum2 = 0

print(list1)
print(list2)

#print the matrix

for i in range(m) :
  for j in range(n) :
   print(a[i][j],end=' ')
  print(list1[i],end='   ')
  print()


for i in list2 :
  print(i,end=' ')
print()
