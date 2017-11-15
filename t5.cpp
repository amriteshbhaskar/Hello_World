#include<bits/stdc++.h>
using namespace std;
int main()
{
	double n,k,t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
    	cin>>n>>k;
    	double l=1.0,r=n,m;
    	while((r-l)>1e-5)
    	{
    		m=(l+r)/2;
    		double temp=pow(m,k);
    		if(temp>n)
    			r=m;
    		else
    			l=m;
    	}
    	printf("%.4lf\n",m);
	}
	
}