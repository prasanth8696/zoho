a = input('enter ')
print(len(a))

arr1 = []
arr2 = []

for i in range(len(a)) :
  if i%2 == 0 :
    arr1.append(a[i])
  else :
   arr2.append(int(a[i]))
sum = ''
for i in range(len(a)//2) :
  sum = sum + arr1[i] * arr2[i]

print(sum)
