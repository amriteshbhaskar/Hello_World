#include<stdio.h>

int main()
{
	char *ptr = "GeeksQuiz"; 
	char *ptr2;
	ptr2=ptr+3;
	
	printf("%c\n", *&*&*ptr);
	printf("%c %ld",*ptr2,(int*)ptr2-(int*)ptr);
	return 0;
}