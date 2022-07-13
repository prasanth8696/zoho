import matrix

def equal(a,b) :

 for i in range(len(a)) :
  for j in range(len(a[0])) :
   if a[i][j] !=  b[i][j] :
     return -1

 return 1
a,m,n = matrix.get_input()

print('******************input matrix ')
matrix.printMatrix(a)
if m == n :
 transpose = matrix.transpose(a)
 print('******************Transpose matrix ')

 matrix.printMatrix(transpose)

 res = equal(a,transpose)

 if res == 1 :
   print('Given matrix is symmetric matrix')
 else :
   print('Given matrix is not a symmetric matrix')


else :
 print("Given matrix is not a symmetric matrix")
