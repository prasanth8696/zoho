import matrix
m = int(input('enter row : '))
n = int(input('enter col : '))




def check(a) :

 for i in range(len(a)) :
   for j in range(len(a[0])) :
      if i < j :
         if a[i][j] == 0 :
           return 'lower triangle matrix...'
      if i>j :
        if a[i][j] == 0 :
           return 'upper triangle matrix...'





a = []
for i in range(m) :
  b = []
  for j in range(n) :
    b.append(int(input('enter ')))
  a.append(b)


print(check(a))


matrix.printMatrix(a)
