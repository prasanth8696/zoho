'''
find given matrix is identity matrix or not

ex : 1 0 0   op : matrix is identity
     0 1 0
     0 0 1

'''

#print the matrix

def printMatrix(a) :
 for i in range(len(a)) :
   for j in range(len(a[0])) :
     print(a[i][j],end=' ')
   print()



#user inputs

m = int(input('enter row '))
n = int(input('enter coloumn '))
a = []

for i in range(m) :
  b = []
  for j in range(n) :
    b.append(int(input('enter ')))
  a.append(b)


value = 0

for i in range(m) :
  for j in range(n) :
    if i == j and a[i][j] != 1 :
      value = 1
      break
    elif i != j and a[i][j] != 0 :
      value = 1
      break


if value == 0 :
  print('given matrix is identity ')
  printMatrix(a)
else :
  print('given matrix is not identity')
