#include<stdio.h>
int main()
{
	int n,t,count;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		t=i;
		count=0;
		while(t!=0)
		{
			if(t%2!=0)
				count++;
			t/=2;
		}
		printf("%d ",count);
	}
}