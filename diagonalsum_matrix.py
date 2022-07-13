# get input from user
#calculate absoute sum of given matrix diagonals
# input must be square matrix ex 4*4


n = int(input('enter '))
sum = 0
sum2 = 0

arr = []

for i in range(n) :
 arr.append([int(j) for j in input().split()])



for i in range(n) :
  for j in range(n) :
   if i == j :
     sum += arr[i][j]
   if i + j  == n - 1 :
     sum2 += arr[i][j]

print(sum)
print(sum2)
print(abs(sum-sum2))
