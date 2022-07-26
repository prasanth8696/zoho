'''
input :
     STR1 --> AXY
     STR2 --> AzsXY
  output is true beacuse str1 is subsequence of str2
'''

s1 = input('enter ')
s2 = input('enter ')

i = 0
j = 0

while(i<len(s1) and j<len(s2)):

 if s1[i] == s2[j] :
   i += 1
   j += 1
 else :
  j += 1


if i == len(s1) :
 print('True ' )

else :
 print('False ')
