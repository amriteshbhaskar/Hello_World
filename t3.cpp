#include<bits/stdc++.h> 
#include<algorithm>
using namespace std;
int main()
{
	multiset <int> ms;
	ms.insert(0);
	multiset <int> :: iterator it;
	for(it = ms.begin(); it != ms.end(); ++it)
	{
		cout << *(it) << " ";
	}
}