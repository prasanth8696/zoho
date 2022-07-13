

# print the matrix 

def printMatrix(a):
  for i in range(len(a))  :
   for j in range(len(a[0])) :
     print(a[i][j],end=' ')
   print()
  print()


# get user input

def get_input() :
 m = int(input('enter row '))
 n = int(input('enter column '))
 a = []
 for i in range(m):
  b = []
  for j in range(n) :
    b.append(int(input('enter ')))
  a.append(b)

 return a,m,n

#transpose of matrix :


def transpose(a) :

  m = len(a)
  n = len(a[0])
  #create empty matrix for transpose matrix
  b = []
  for i in range(n) :
   c = []
   for j in range(m) :
     c.append(0)
   b.append(c)

  for i in range(m):
    for j in range(n) :
       b[j][i] = a[i][j]

  return b
