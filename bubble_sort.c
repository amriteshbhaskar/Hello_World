#include<stdio.h>

int main()
{	
	int a[100],n,flag=1;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		scanf("%d",&a[i]);
	while(flag==1)
	{
		flag=0;
		for(int i=0;i<n-1;i++)
		{
			if(a[i]>a[i+1])
			{
				a[i]=a[i]+a[i+1];
				a[i+1]=a[i]-a[i+1];
				a[i]=a[i]-a[i+1];
				flag=1;
			}
		}
	}
	for(int i=0;i<n;i++)
		printf("%d",a[i]);
}

