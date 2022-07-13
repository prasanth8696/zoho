no_bits = int(input('enter '))

arr = [int(i) for i in input().split()]

new = []

for i in range(len(arr)) :
  if arr[i] == arr[i+1] :
    new.insert(i+2,0)



print(new)
