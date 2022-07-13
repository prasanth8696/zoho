'''

print alternate  manner 
 ex :
     1 2 3       op : 1 2 3
     4 5 6            6 5 4
     7 8 9            7 8 9
'''

m = int(input('enter row '))
n = int(input('enter column '))
a= []
for i in range(m) :
 c = []
 for j in range(n) :
  c.append(int(input('enter ')))
 a.append(c)
 #print the matrix

for i in range(m):
 for j in range(n) :
  print(a[i][j],end=' ')
 print()

print()

row_start = 0
col_start = 0
row_end = len(a)
col_end = len(a[0])
while(True) :

#left to right 
 for i in range(col_start,col_end) :
   print(a[row_start][i],end=' ')
 print()
 row_start += 1

 if row_start > row_end-1 :
  break

#right to left
 for i in range(col_end-1,col_start-1,-1) :
   print(a[row_start][i],end=' ')
 print()

 row_start += 1

 if row_start > row_end-1 :
  break


#second method 


'''
for i in range(m) :
 k = m-1
 if i%2 == 0 :
   for j in range(n): 
   print(a[i][j],end=' ')
 print()

 else :
  for j in range(n) :
    print(a[i][k],end=' ')
    k = k - 1









