
m = int(input('enter row '))

n = int(input('enter column '))
a = []
for i in range(m) :
  b = []
  for j in range(n) :
   b.append(int(input('enter ')))
  a.append(b)

#print  the matrix 
for i in range(m) :
  for j in range(n) :
   print(a[i][j],end=' ')
  print()
#create empty transpose matrix
b = []
for i in range(n) :
  c = []
  for j in range(m) :
    c.append(0)
  b.append(c)

#matrix transpose

for i in range(m) :
  for j in range(n) :
   b[j][i] =a[i][j]



#anticlockwise --> reverse the transpose matrix

print('clockwise matrix ')
for i in range(len(b)) :

 for j in range(len(b[0])-1,-1,-1) :
   print(b[i][j],end=' ')
 print()

