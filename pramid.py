#qn available in alogo tamila

#method1--> concept based


n = int(input('enter '))

for i in range(n):
 for j in range(i+1) :
   print(' ',end='')

 for j in range(i,n):
    print('*',end='')

 for j in range(i+1,n):
   print('*',end='')
 print()


#trick --> Easy Method

space = 1
star = n*2-1

for i in range(n):
 print(space * ' ',end='')
 print(star * '*',end='')
 print()
 space += 1
 star -= 2

