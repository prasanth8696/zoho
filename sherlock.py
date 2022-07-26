#available in code.io
def check():
 arr = list(map(int,input().split()))


 lsum = sum(arr)

 rsum = 0

 for i in range(len(arr)-1,-1,-1):
    lsum = lsum - arr[i]
    if lsum ==rsum :
      return arr[i]
    rsum = rsum + arr[i]



 return -1

print(check())

