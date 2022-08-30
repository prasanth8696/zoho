a = input().strip()

a = a + '$'

sum = 0

num = 0

for i in range(len(a)):
 if a[i].isnumeric() :
   num = num *10 + int(a[i])
 else :
  sum += num
  num = 0



print(sum)
