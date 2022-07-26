
#include<stdio.h>

int sum(n){
 int sum = 0,last=0;
 while(n>0){
  last = n%10;
  sum += last;
  n = n/10;

  }
return sum;
 }
int main()
{ int n,i,a[50],h= 0,b[50]
printf("enter array elements ");

for (i= 0;i<n;i++){
 scanf("%d",&a[i]);
 }

for (i=0;i<n;i++){
  b[h] = sum(a[i]);
  h++;
  }

for (i=0;i<n;i++){
  for(j=0;j<n;j++){
   if b[i] > b[j]:
     temp = a[i];
     



return 0;
}
//incomplete
