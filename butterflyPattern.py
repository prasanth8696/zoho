#qn available in alogo tamila chennal

#concept based

n = int(input('enter '))

for i in range(n):
  for j in range(n):
    if i >= j :
     print('*',end='')
    else :
     print(' ',end='')


  for j in range(n-1,-1,-1):
   if i >= j :
    print('*',end='')
   else :
    print(' ',end='')

  print()

for i in range(n):
  for j in range(n-1,-1,-1) :
   if  j >= i :
    print('*',end='')
   else :
    print(' ',end='')


  for j in range(n):
    if j >= i :
     print('*',end='')
    else :
     print(' ',end='')
  print()


print()

# trick easy method

space = n*2
for i in range(1,n+1):
  space -= 2
  print(i*'*',end='')
  print(space * ' ',end='')
  print(i * '*',end='')
  print()


for i in range(n,0,-1):
  
  print(i*'*',end='')
  print(space * ' ',end='')
  print(i * '*',end='')
  space += 2
  print()
