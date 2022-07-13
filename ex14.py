st = input('enter ')

count = ''
for i in range(len(st)) :


  for j in range(i+1,len(st)) :
    if st[j] >= '0' and st[j] <= '9':
#      print(type(st[j]))
 #     print(type(count))
      count = count + st[j]
      continue
    break
  position = j -1
  print(count)
  print(st[i]*int(count))
  i = position
  count = ''
