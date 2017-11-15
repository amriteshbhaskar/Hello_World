t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    count=0
    for i in range(n):
        s=input().split()
        while(j<len(s)-k):
    		f=1
            for l in range(j+1,j+k+1):
                if s[l]!=s[j]:
                    count+=1
                else:
                	if f=1:
                		j=l-1
                		f=0
            j+=1
    print(count)
