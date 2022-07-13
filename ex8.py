inp =[int(i) for i in input().split(' ')]


def fun(inp) :

 max = 0 
 for i in inp:
  if max< i :
    max = i
    index = inp.index(i)
 print(max)
 for i in inp :
  if max == i:
   continue
  if i*2 > max :
   return -1
 return index



print(fun(inp))


