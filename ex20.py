'''
input = a4k3b2 output = aeknbd


'''

str  = input('enter ')

def string(s) :
 op = ''
 temp = s[0]
 for i in range(len(s)) :

  if s[i].isnumeric():
     val = ord(temp) + int(s[i])
     op = op + chr(val)
  else :
   op += s[i]
   temp = s[i]

 return op




print(string(str))
