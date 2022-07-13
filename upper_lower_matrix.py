m = int(input('enter row '))
n = int(input('enter column '))

a = []
for i in range(m) :
 c = []
 for j in range(n) :
  c.append(int(input('enter ')))
 a.append(c)

print('1 --> copy lower triangle values to upper triangle')
print('2 --> copy upper triangle values to lower triangle')
print('3 --> swap two triangle values ')
no = int(input())

def printMatrix(a) :
  for i in range(len(a)) :
    for j in range(len(a[0])) :
     print(a[i][j],end=' ')
    print()

def upper_lower(a,no,m,n) :
#print matrix
 printMatrix(a)
 print()


# get upper triangle and lower triangle
 list1 = []
 list2 = []

 for i in range(m) :
  for j in range(n) :
    if i<j :
     list1.append(a[i][j])
    if i>j :
     list2.append(a[i][j])


 if no == 1:
  # copy upper triangle to lower triangle
  k = 0
  for i in range(m) :
   for j in range(n) :
     if i > j :
      a[i][j] = list1[k]
      k = k + 1
  print('copy lower to upper ')
  print()
  printMatrix(a)
# copy lower triangle to upper triangle
 elif no == 2 :
   k = 0
   for i in range(m) :
     for j in range(n) :
      if i<j :
        a[i][j] = list2[k]
        k = k + 1
   print('copy upper to lower ')
   print()
   printMatrix(a)


#swap two triangle values
 elif no == 3 :
   k = 0
   q = 0
   for i in range(m) :
     for j in range(n) :
      if i<j :
        a[i][j] = list2[k]
        k = k + 1
      if i > j :
        a[i][j] = list1[q]
        q = q + 1
   print('swap to two triangle values')
   print()
   printMatrix(a)

 else :
  print('invalid choice')

#call the function 
upper_lower(a,no,m,n)
