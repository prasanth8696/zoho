#available in code.io chennal



s = input('enter string ')

n = int(input('enter rotation value '))

temp = ''

for i in range(len(s)):

 if s[i].isalpha() :
    if s[i].isupper():
       val = ord(s[i]) + n
       if val > 90 :
          val = val - 90
          val = 64 + val
       temp = temp + chr(val)
       val = 0
    else :
      val = ord(s[i]) + n
      if val > 122 :
        val = val - 122
        val = 96 + val
      temp = temp + chr(val)
      val = 0
 else :
   temp = temp + s[i]


print(temp)
