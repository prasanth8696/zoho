'''
sparse means no of zero elements more than total elements in a matrix

for example :
  a = 1 0 0
      0 0 1
      5 6 0 here no of zero elements is 5 so it is more than half of the
total elements

output = matrix is sparse

'''

def printMatrix(a):
  for i in range(len(a)) :
    for j in range(len(a[0])) :
     print(a[i][j],end=' ')
    print()


#user inputs

m = int(input('enter row '))
n = int(input('enter column '))
a = []
for i in range(m):
 c = []
 for j in range(n) :
   c.append(int(input('enter ')))
 a.append(c)

count = 0

for i in range(m):
  for j in range(n):
    if a[i][j] == 0 :
     count = count + 1

if count > m*n //2 :
  print('matrix is sparse')
  printMatrix(a)
else :
  print('matrix is not a sparse')
  printMatrix(a)
