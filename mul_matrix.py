X = [[1, 7, 3],[3, 5, 6],[6, 8, 9]]

Y = [[1, 1, 1, 2],[6, 7, 3, 0],[4, 5, 9, 1]]


def mul_matrix(X,Y) :
 result = []
 a = []
 sum = 0
 if len(X[0]) != len(Y) :
  return 'matrix mul opertion cannot apply for this matrices'

 for i in range(len(X)) :
   for j in range(len(Y[0])) :
    for k in range(len(Y)) :
      sum = sum + X[i][k] * Y[k][j]
      print(sum)
    a.append(sum)
    sum = 0
   result.append(a)


 print(result)


mul_matrix(X,Y)
