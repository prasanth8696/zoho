#chocolate factory empty packets



arr = [int(i) for i in input().split()]
count = 0
for i in arr :
 if i == 0 :
  count += 1
  index = arr.index(i)
  del arr[index]
for i in range(count) :
  arr.append(0)



print(arr)
