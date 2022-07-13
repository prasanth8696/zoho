str = input('enter ').split(' ')


def palindrome(str) :
  word = ''
  for i in str :
    word = i + word
  if str == word :
    return True
  return False

final_word = ''
for i in str :
  res = palindrome(i)
  if res != True :
    final_word = final_word + ' ' + i

print(final_word)
