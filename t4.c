#include <stdio.h>
#include<curses.h>
int main()
{
	FILE *f;
	char ch[1000];
	f=fopen("test.txt","w");
	fgets(ch,1000,f);
	fclose(f);

}