a = list(map(int,input().strip().split()))


i = 0
j= len(a) - 1


while(i<j) :
 if a[i] == 0 and a[j] != 0 :
   a[i],a[j] = a[j],a[i]
   j  -= 1
   i += 1

 if a[i] != 0 :
  i += 1
 if a[j] == 0 :
  j -= 1


print(a)
