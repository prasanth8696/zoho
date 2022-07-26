#include<stdio.h>
#include<string.h>
int main()
{

int n,i;
char a[100];
printf("enter ");
scanf("%d",&n);

gets(a);

int len = 0;
int count = 0;

for(i=0;i!='\0';i++)
{
 len++;
 if  ((strcmp(a[i],"a") == 0 )
 {
   count++;
 }
}

count = (n/len) * count;

int temp = 0;
temp = n%len;

for(i=0;i<temp;i++)
{
 if ((strcmp(a[i],"a") == 0)
 {
  count++;
 }

printf("%d",count);
}





return 0;
}
