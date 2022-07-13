a = input('enter ')

list = []

for i in a :
 if i.isalpha() :
  continue
 list.append(i)

stack = []

for i in list :
 if list[0] == ')' :
  stack.append(i)
  break
 if i == '(' :
  stack.append(i)
 elif i == ')' :
   stack.pop()


if len(stack) == 0 :
 print('balanced')
else :
 print('unbalanced')
