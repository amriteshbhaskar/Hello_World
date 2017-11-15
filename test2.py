t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    s=input()
    
    for _ in range(q):
        l,r=map(int,input().split())
        a=list()
        count=0
        for j in range(27):
            a.append(0)
        for i in s[l-1:r]:
            a[i-96]+=1
        for i in range(1,27):
            if count==0:
                count=1
            else:
                count=2
        if count==0 or count==1:
            print("YES")
        else:
            print("NO")
