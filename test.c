#include<stdio.h>
#include<string.h>

int main()
{
	char s[101];	int flag=0,count=1;
	scanf("%s",s);
	for(int i=0;i<strlen(s);i++)
	{
		if(i>0)
			if(s[i]==s[i-1])
				count++;
			else
				count=1;
		if(count==6)
		{
			flag=1;
			break;
		}
		
	}
	if(flag==1)
		printf("Sorry, sorry!");
	else
		printf("Good luck!");
}
