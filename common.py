arr1 = list(map(int,input().split()))

arr2 = list(map(int,input().split()))

arr3 = list(map(int,input().split()))

dict = {}

for i in arr1:
  if i not in dict:
     dict[i] = 1
  else :
    dict[i] += 1

for i in range(len(arr1)):
  if arr2[i] in dict and arr3[i] in dict :
     print(arr2[i],end=' ')


print()
