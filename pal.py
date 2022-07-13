def palindrome(num) :
 reverse = 0
 temp = num
 while(num>0) :
  laat = num%10
  reverse = reverse *10 + laat
  num = num //10
 if temp == reverse :
  print('palindrome')
 else :
  print('not')


a = int(input())
palindrome(a)
