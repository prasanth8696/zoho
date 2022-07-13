'''
swap first and last column elements

ex :
    1 2 3    op: 3 2 1
    4 5 6        6 5 4
    7 8 9        9 8 7

'''

m = int(input('enter row '))
n = int(input('enter col '))
a = []

for i in range(m) :
  c = []
  for j in range(n) :
    c.append(int(input('enter ')))
  a.append(c)

#column interchange

for i in range(m) :
  temp = a[i][0]
  a[i][0] = a[i][n-1]
  a[i][n-1] = temp

for i in range(m):
 for j in range(n) :
   print(a[i][j],end=' ')
 print()
