#code available in code.io chennal
#automorphic number

n = input('enter ')

k = len(n)

sq = int(n)**2

len = len(str(sq)) - 1
temp = ''

while(k) :

  last = str(sq)[len]
  temp = last + temp
  k = k - 1
  len = len - 1


if int(temp) == int(n) :
  print("yes")
else :
  print('No')


'''
def anotherMathod(n):
 last_two_digit = sq%pow(10,k)

 
 ex 25 sqaure value = 625
        --> 625% pow(10,here 25 lenth is 2) so 100
        -->  625%100 >>> give last two digit in this case
     '''
