n = int(input('enter length '))
val = [int(i) for i in input().split(' ')]

def no_occurence(list) :
  dict = {}
  for i in list :
   count = 0
   for j in list:
    if i == j :
     count = count + 1
    dict[i] = count
  temp = 0
  for  i,j in dict.items() :
    temp += 1
    if temp<len(dict) : 
     print(str(i)+'({})'.format(j),end =',')
    else :
     print(str(i)+'({})'.format(j),end ='')
  print()


if n == len(val) :
  no_occurence(val)
else :
 print('wrong input')
