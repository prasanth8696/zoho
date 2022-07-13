str = input('enter ')

a = []
for i in str :
  a.append(i)

res_max = 0

for i in a :
  count = 0
  for j in a :
   if i == j :
    count += 1
  if count > res_max :
    res_alpha = i
    res_max = count

print(res_alpha ,res_max)

