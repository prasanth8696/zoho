inp = int(input('enter '))

m = (inp+1)/2
print(m)
print()

for i in range(1,inp+1) :
  for j in range(1,inp+1) :
    if i == j :
      if i<m:
        print(inp-i+1,end='')
      else :
        print(i,end='')
    elif i+j == inp+1 :
      if i<m :
        print(i,end='')
      else :
        print(j,end='')
    else :
     print('  ',end='')
  print('')


