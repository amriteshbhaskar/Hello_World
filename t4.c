#include<stdio.h>

void pnt(int);

int main()
{
    pnt(100);
    return 0;
}



void pnt(int n)
{
    n>0?printf("%d %d",n,pnt(n-1)):printf(" ");
}