x,y=map(int,input())
a[x][y]=1
if flag==1:
    for i in range(3):
        try:
            if sum(a[i][j] for j in range(3))==2:
            for k in range(3):
                if a[i][k]!=1:
                    a[i][k]==1
                    flag=0
        except:
            pass
if flag==1:
    for i in range(3):
        try:
            if sum(a[j][i] for j in range(3))==2:
            for k in range(3):
                if a[k][j]!=1:
                    a[k][i]==1
        except:
            pass

    


                