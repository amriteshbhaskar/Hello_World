#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int min_fun(int *a,int b)
{

}
int main()
{
	char s[200];
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int ns=0,nu=0,nv=0,no=0,nj=0,ni=0,nt=0;
		cin>>s;
		for(int j=0;j<strlen(s);j++)
		{
			char l=s[j];
			if(l=='s')
				ns++;
			if(l=='u')
				nu++;
			if(l=='v')
				nv++;
			if(l=='o')
				no++;
			if(l=='j')
				nj++;
			if(l=='i')
				ni++;
			if(l=='t')
				nt++;

		}
		int arr[201]=[ns,nu,nv,no,nj,ni,nt];
		cout<<"SUVO = "<<min()<<", SUVOJIT = "<<min(ns,nu,nv,no,nj,ni,nt)<<endl;

	}
	
}