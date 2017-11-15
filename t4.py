n=int(input())
a=list(map(int,input().split()))
b=[a[0]]
for i in range(1,n):
    b.append(a[i]+b[i-1])
q=int(input())
for _ in range(q):
    t=int(input())
    i=0
    while(b[i]<t):
        i+=1
    print(i+1)
