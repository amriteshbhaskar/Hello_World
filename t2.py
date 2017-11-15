t=int(input())
l={'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6,'0':6}
for _ in range(t):
    n=int(input())
    a=list(input().split())
    min=7*(10**6)
    ans='0'
    for i in a:
    	sum=0
        for j in i:
        	sum+=l[j]
        if min>sum:
            min=sum
            ans=i
    print(ans)        
