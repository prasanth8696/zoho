#available in  alogo tamila chennal


n = int(input('enter '))
len = (n+1)//2
print(len)
for i in range(len) :
   for j in range(len-1,-1,-1) :
     if j>=i :
      print('*',end='')
     else :
      print(' ' ,end= '')

   for j in range(len) :
     if j>=i :
      print('*',end='')
     else :
      print(' ' ,end= '')
   print()

for i in range(1,len) :
 for j in range(len):
   if i>=j :
    print('*',end='')
   else:
    print(' ',end='')


 for j in range(len-1,-1,-1):
   if i>=j :
    print('*',end='')
   else:
    print(' ',end='')
 print()
