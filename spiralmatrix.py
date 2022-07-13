

a = [
     [1,2,3,4],
     [14,15,16,5],
     [13,20,17,6],
     [12,19,18,7],
     [11,10,9,8]
                 ]

row_start = 0

row_end = len(a)

col_start = 0

col_end = len(a[0])

while(row_start <= row_end and col_start <= col_end) :

# print top (left to right)
 for i in range(col_start,col_end) :
   if i < col_end :
    print(a[row_start][i],end=' ')
 row_start += 1

# print (top to bottom)

 for  i in range(row_start,row_end) :
   if i < row_end :
    print(a[i][col_end-1],end=' ')
 col_end -= 1

#print bottom (right to left)

 for i in range(col_end-1,0,-1) :
  if i >= col_start : 
   print(a[row_end-1][i],end=' ')
 row_end -= 1

#print bottom to left

 for i in range(row_end-1,row_start-1,-1) :
    print(a[i][col_start],end=' ')
 col_start += 1
print()
print(row_start)
print(row_end)
print(col_start)
print(col_end)
