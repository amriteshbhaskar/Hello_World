#include <stdio.h>
#include<string.h>

int merge(int arr[],int l,int m,int r)
{
	int a=l,b=m+1,i,c[100];
	for(i=l;a<=m&&b<=r;i++)
	{
		if(arr[a]<arr[b])
			c[i]=arr[a++];
		else
			c[i]=arr[b++];
	}
	while(a<=m)
		c[i++]=arr[a++];
	while(b<=r)
		c[i++]=arr[b++];
	for(int j=l;j<=r;j++)
		arr[j]=c[j];
}

int merge_sort(int arr[],int l,int r)
{
	if(l<r)
	{
		int m=(l+r)/2;
		merge_sort(arr,l,m);
		merge_sort(arr,m+1,r);
		merge(arr,l,m,r);
	}
	else
		return 0;
}

int main()
{
	int arr[]={0,2,66,2,4,22,1,53,13};
	merge_sort(arr,0,8);
	for(int i=0;i<9;i++)
		printf("%d ",*(arr+i));
}


