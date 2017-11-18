#include<stdio.h>
int swap(int *a,int *b)
{
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
}

int part(int *a,int l,int u)
{
	int p=a[u];
	int t=l-1;
	for(int i=l;i<u;i++)
	{
		if(a[i]<p)
		{
			t++;
			swap(&a[t],&a[i]);
		}
		for(int j=l;j<u+1;j++)
			printf("%d ",a[j]);
		printf("\n");
	}
	swap(&a[t+1],&a[u]);
	return t+1;
}

int main()
{
	int a[100],n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		scanf("%d",a+i);
	part(a,0,n-1);
	for(int i=0;i<n;i++)
		printf("%d	",a[i]);
	printf("\n");
}