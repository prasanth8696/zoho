s = input('enter string ')

temp = ''
for i in range(len(s)-1,-1,-1):
  temp = s[i] + temp
  if s[i] in ('a','e','i','o','u','A','E','I','O','U') :
    print(temp)
    temp = ''
