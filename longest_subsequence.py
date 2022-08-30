arr = list(map(int,input().split()))


temp = [1] *len(arr)

arr_list = []

for i in range(1,len(arr)) :
  b = [i]
  for j in range(0,i+1) :
     if arr[j] >=arr[i] :
        temp[i] = temp[i] + 1
        b.append(arr[j])
  arr_list.append(b)

maxi = max (temp)
print(arr_list)
for i in arr_list :
  if len(i) == maxi :
    print(i)
