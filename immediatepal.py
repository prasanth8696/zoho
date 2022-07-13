# find  immediate palindrome



def palindrome(num) :
 num2 = num
 reverse = 0
 while(num>0) :
  last  = num%10
  reverse = reverse*10 + last
  num = num//10
#  print(num,reverse)
 if num2 == reverse :
  return 1
 else :
  return -1



num = int(input('enter '))
while(True) :
 num += 1
 res = palindrome(num)
 if res == 1 :
  print(num)
  break
