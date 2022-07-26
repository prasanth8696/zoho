#available in code.io
#missing numbers

#get input 

arr = list(map(int,input('enter ').split()))

brr = list(map(int,input('enter ').split()))
a = []

dict = {}

for i in arr :
 if i in dict :
   dict[i] = dict[i] + 1
 else :
   dict[i] = 1
#print(dict)
for i in range(len(brr)) :
  if brr[i] in dict :
     dict[brr[i]] = dict[brr[i]] - 1
  else :
   a.append(brr[i])


for i in dict.keys() :
  if dict[i] != 0 :
    a.append(i)

print(a) 
