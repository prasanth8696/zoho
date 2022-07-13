arr = [int(i) for i in input().split()]

pos,neg,neutral = 0,0,0

for i in arr :
  if i == 0:
   neutral += 1
  elif i > 0 :
    pos += 1
  else :
   neg += 1

n = len(arr)

print(pos/n,end=' ')
print(neutral/n,end=' ')
print(neg/n)
