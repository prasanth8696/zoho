'''
find given matrix is magic square matrix or not

condition : sum of row and sum of col all are equal

step 1 : find diagnonals sum if not squal simply return -1

step 2 : if equal find sum of rows and col and check equal or not if not return -1

'''

def magicsquare(a) :

#diagonal check 
 dig1 = 0
 dig2 = 0 

 for i in range(len(a)) :
   for j in range(len(a[0])) :
    if i == j :
     dig1 = dig1 + a[i][j]
    if i+j == m-1:
     dig2 = dig2 + a[i][j]

 if dig1 != dig2 :
   return -1

 col = 0
 row = 0
 for i in range(m) :
   for j in range(n) :
     row += a[i][j]
     col += a[i][j]
   if row != dig1 :
       return -1
   elif col != dig1 :
       return -1
   else :
      row = 0
      col = 0

 return 1


import matrix


m = int(input('enter row '))
n = int(input('enter column '))

a = matrix.get_input(m,n)

res = magicsquare(a)

if res == 1:
 print('given matrix is magicSquareMatrix')
 matrix.printMatrix(a)
else :
 print('given matrix is not a magicSquareMatrix')
 matrix.printMatrix(a)


