//replace the value of row and col =1 corresponding a[i][j] == 1
// ex 1 0    op : 1 1
//    0 0         1 0


#include<stdio.h>

int main()
{

//user inputs 
int a[100][100],i,j,m,n,row,col;

printf("enter row ") ;
scanf("%d",&m);
printf("enter column ");
scanf("%d",&n);

for (i= 0;i<m;i++)
 { for(j=0;j<n;j++)
   {

       printf("enter ");
       scanf("%d",&a[i][j]);

   }

 }
//print user matrix
//print the matrix
for(i=0;i<m;i++)
{
 for(j=0;j<n;j++)
 {
    printf("%d",a[i][j]);
   }
 printf("\n") ;

 }
printf("\n");

//find the a[i][j] == 1 and find corresponding row and col

for(i=0;i<m;i++)
{
  for(j=0;j<n;j++)
  {
     if(a[i][j]==1)
     { row = i;
       col = j;
     }

  }


}

//repalce 1 in row and col of a[i][j] == 1

for(i=0;i<m;i++)
{
 for(j=0;j<n;j++)
 {
   if(row==i || col==j)
   {
     a[i][j] = 1;
   }

 }


}
printf("result matrix\n");
//print the result matrix
for(i=0;i<m;i++)
{
 for(j=0;j<n;j++)
 {
    printf("%d",a[i][j]);
   }
 printf("\n") ;

 }






return 0;
}
