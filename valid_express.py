a = input('enter :')


def check(a):
 stack = []

 for i in range(len(a)) :

  if a[i] == '(' :
    stack.append(a[i])
  elif a[i] == ')':
    if len(stack) > 0 :
      stack.pop()
    else :
      return -1
  if a[i] in  ['+','-','*','/']:
      if ord(a[i-1])>=97 and ord(a[i-1])<=122 and ord(a[i+1])>=97 and ord(a[i+1])<=122 :
          pass
      else :
       return -1

 if len(stack) == 0 :
    return 1
 else :
    return -1



res =  check(a)

if res == 1 :
  print('Valid...')
else :
  print('Not Valid...')



