#include<stdio.h>

int main()
{
	char c[100];
	fgets(c,100*sizeof(char),stdin);
	printf("%s",c);
}
