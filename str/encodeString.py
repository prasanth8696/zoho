'''
ip = aaaabbbccczz op = 4a3b3c2z

'''

def encode(s) :

 s = s + '$'
 count = 1
 op = ''

 for i in range(1,len(s)) :
   if s[i] == s[i-1] :
     count += 1
   else :
     op = op + (str(count) + s[i-1])
     count = 1

 return op


def decode(s):
 s = s + '&'
 char = s[0]
 count = ''
 op = ''

 for i in range(1,len(s)) :
  if s[i].isnumeric() :
   count += s[i]
  else :
    op += int(count) * char
    char = s[i]
    count = ''
 return op




print('1.str encode ')
print('2.str decode')
choice = int(input('enter 1 or 2-->  '))
st = input('enter str -->  ')

if choice == 1:

 print(encode(st))
if choice == 2:
  print(decode(st))
