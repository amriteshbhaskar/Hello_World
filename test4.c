
int main()
{
    int t,n,q,l,r;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
    	char s[100];
    	scanf("%d %d",&n,&q);
    	scanf("%s",s);
    	int count=0;
    	for(int j=0;j<q;j++)
    	{
			count=0;
			int a[27]={0};
			scanf("%d %d",&l,&r);
            
			for(int k=l-1;k<r;k++)
				a[s[k]-96]++;
			for(int k=1;k<27;k++)
				if(a[k]%2!=0)
				{
				if(count==0)
					count=1;
				else
					count=2;
				}

    		if(count==1||count==0)
    			printf("YES\n");
    		else
    			printf("NO\n");
    	}
    }
    return 0;
}