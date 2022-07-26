#available in alogotamila chennal



n = int(input('enter '))

len = n//2 + 1

for i in range(len) :
  for j in range(len-1,-1,-1) :
   if j==i :
    print('*',end='')
   else :
    print(' ',end='')

  for j in range(1,len) :
   if j==i :
    print('*',end='')
   else :
    print(' ',end='')
  print()


for i in range(1,len):
  for j in range(0,len-1):
   if i==j :
    print('*',end='')
   else :
    print(' ',end='')


  for j in range(len-1,-1,-1):
   if i== j :
     print('*',end='')
   else :
    print(' ',end='')
  print()

