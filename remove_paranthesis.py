a = input('enter : ')


stack = []

s = list(a)


for i in range(len(s)):


  if s[i] == '(' :
     stack.append(i)
  elif s[i] == ')' :
     if len(stack) > 0 :
       stack.pop()
     else :
       s[i] = ''

for i in stack :
  s[i] = ''


print(''.join(s))
