a = input('enter srring ')

count = 1
stack =[]
res = []
for i in a :
  if i == '(':
    stack.append(count)
    res.append(count)
    count += 1
  if i == ')' :
    res.append(stack.pop())

for i in res :
 print(i,end=' ')
