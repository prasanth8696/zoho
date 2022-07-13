//given string contain two color like "RGRGR"
//find the minimum way to change same color
//ex "RGRGR" 
// if you want convert all color into green 3 step need
//red 2steps need so ouput is 2


#include<stdio.h>
#include<string.h>
int main()
{
char a[30],i,count=0,count2=0 ,temp = -1;

printf("enter the string ");
scanf("%s",a);
int len;
//strlwr(a);
len = strlen(a);

for(i=0;i<len;i++)
{ 
  if (a[i] =='R')
  {
    count += 1;

  }
  else
  {
   count2 += 1; 
  }


} 

if(count<count2)
{
printf("%d",count);
}
else
{
printf("%d",count2);
}
return 0;


}
