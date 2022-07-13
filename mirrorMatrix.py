import matrix
"""

print mirror matrix of given matrix 
ex : 1 2 3  op : 3 2 1
     4 5 6       6 5 4
     7 8 9       9 8 7
"""

a,m,n = matrix.get_input()

matrix.printMatrix(a)


# mirror the matrix
print('Mirror matrix ')
for i in range(m) :
 for j in range(n-1,-1,-1) :
   print(a[i][j],end=' ')
 print()

