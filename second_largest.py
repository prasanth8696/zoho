a = list(map(int,input().strip().split()))


max1 = 0
max2 = 0
for i in range(len(a)) :
 if max1 < a[i] :
   max2 = max1
   max1 = a[i]

 elif max2 < a[i] :
   max2 = a[i]



print(max1,max2)

