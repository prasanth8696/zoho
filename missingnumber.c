//find the missing elemnet in the given array
//array contains 1 to N elements
//formula n(n+1)/2
// ex [1,2,3,5]  op missing element 4
// original sum - actual sum = missing element



#include<stdio.h>

int main()
{

int a[50],sum1=0,sum2=0,n,i;

printf("enter the n ");
scanf("%d",&n);
//printf("enter the array elements ");
for(i=0;i<n-1;i++)
{

scanf("%d",&a[i]);

}

for (i=0;i<n;i++)
{
sum1=  sum1 + a[i];
}

sum2 = n*(n+1)/2;

printf("%d",(sum2-sum1));


return 0;}

