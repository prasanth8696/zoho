''' Alternate sorting: Given an array of integers, rearrange the array in such a way that the first element is first maximum and second element is first minimum.

Eg.) Input  : {1, 2, 3, 4, 5, 6, 7}
         Output : {7, 1, 6, 2, 5, 3, 4}
'''


list = [int(i) for i in input().split()]

max = 0

for i in range(len(list)) :
 for j in range(len(list)-1) :
   if list[j] < list[j+1] :
    temp = list[j]
    list[j] = list[j+1]
    list[j+1] = temp


print(list)
list2 = list.copy()
list2.reverse()
print(list2)

for i in range((len(list)//2)+1) :
 if list[i] == list2[i] :
  print(list[i],end='')
  print()
  break
 print(list[i],end=' ')
 print(list2[i],end=' ')
