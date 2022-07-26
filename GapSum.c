#include<stdio.h>

int main()
{ int n,a[100],i,j,gap,sum=0;
scanf("%d",&n);
printf("enter the array elements ");
for (i=0;i<n;i++)
{
 scanf("%d",&a[i]);


}
printf("enter ");
scanf("%d",&gap);

for (i=0;i<gap;i++)
{
 for(j=i;j<n;j=j+gap)
 {
   sum += a[j];


 }
printf("%d ",sum) ;
sum = 0;

}



return 0;
}
