'''
    0
   101
  21012
 3210123


n== 3

'''
n = int(input('enter '))

for i in range(n) :
  for j in range(i,n) :
   print(' ',end='')
  for j in range(i,-1,-1) :
   print(j,end='')
  for j in range(1,i+1):
   if i >= 1 :
    print(j,end='') 
  print()

