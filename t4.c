#include <stdio.h>
#include <stdlib.h>
int main()
{
	int *p;
	p=(int*)calloc(10,sizeof(int));
	for(int i=0;i<10;i++)
	{
		scanf("%d",p+i);
		printf("%d",*(p+i));
	}
	p=realloc(p,5);
	for(int i=10;i<15;i++)
	{
		scanf("%d",p+i);
	}

	for(int i=0;i<15;i++)
	{
		printf("%d",*(p+i));
	}


}