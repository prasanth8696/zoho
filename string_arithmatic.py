a = input('enter ')

value = []
operator = []
def isvalue(char) :
 return char.isnumeric() 

for i in  a :
 if isvalue(i) :
   value.append(int(i))
 else :
   operator.append(i)

res = value[0]

for i in range(1,len(value)) :
  if operator[i-1] == '+' :
   res += value[i]
  elif operator[i-1] == '-' :
   res -= value[i]
  elif operator[i-1] == '*' :
   res *= value[i]
  else :
    res /= value[i]


print(res)



