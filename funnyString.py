#available in code.io
#funny string


s = input('enter ')

rev =  s[::-1]
a = []
b = []
for i in range(len(s)-1):

 temp =abs(ord(s[i]) - ord(s[i+1]))
 a.append(temp)

 temp1 = abs(ord(rev[i]) - ord(rev[i+1]))
 b.append(temp1)


if a == b :
 print("funny") 
else :
 print("not funny")
