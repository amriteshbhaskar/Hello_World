import random
a=[[0 for i in range(3)]for j in range(3)]


for i in range(3):
    for j in range(3):       
        print('*',end=' ')
    print('')
print('\n\n')


end='n'
k=1
while end=='n' and k<=5:
    x,y=map(int,input().split())
    a[x][y]=1
    flag=1
    
    
    if flag==1 and end=='n':        #To check for possible horizontal moves
        for i in range(3):
            if flag==1:
                try:
                    if sum(a[i][j] for j in range(3))==2:
                        for k in range(3):
                            if a[i][k]!=1:
                                a[i][k]='a'
                                flag=0
    
                except:
                    pass
            else:
                break
    
    
    
    
    if flag==1 and end=='n':        #To check for possible vertical moves
        for i in range(3):
            if flag==1:
                try:
                    if sum(a[j][i] for j in range(3))==2:
                        for k in range(3):
                            if a[k][i]!=1:
                                a[k][i]='a'
                                flag=0
                except:
                    pass
            else:
                break
    
    
    
    
    if flag==1 and end=='n':        #To check for possible diagonal(left to right) moves
        try:
            if a[0][0]+a[1][1]+a[2][2]==2:
                for i in range(3):
                    if a[i][i]!=1:
                        a[i][i]='a'
                        flag=0
            
        except:
            pass

    
    
    
    if flag==1 and end=='n':        #To check for possible diagonal(right to left) moves
        try:
            if a[0][2]+a[1][1]+a[2][0]==2:
                for i in range(3):
                    if a[i][2-i]!=1:
                        a[i][2-i]='a'
                        flag=0
        except:
            pass

    
    
    
    '''if flag==1 and end=='n':        #Random move
        s=[]
        for i in range(3):
            for j in range(3):
                if a[i][j]==0:
                    s+=[[i,j]]
        if len(s)==0:
            print("Draw")
            end='yes'
        else: 
            n=random.randint(0,len(s)-1)
            a[s[n][0]][s[n][1]]='a' '''
    
    
    
    
    if end=='n':        #To check is the player won
        for i in range(3):
            if a[i][0]==1 and a[i][1]==1 and a[i][2]==1:
                print("You Won")
                flag=0
                end='yes'
    
    
    
    
    if end=='n':
        for i in range(3):
            if a[0][i]==1 and a[1][i]==1 and a[2][i]==1:
                print("You Won")
                flag=0
                end='yes'
    
    
    
    
    if end=='n':
        if a[0][0]==1 and a[1][1]==1 and a[2][2]==1:
            print("You Won")
            flag=0
            end='yes'
    
    
    
    
    if end=='n':
        if a[0][2]==1 and a[1][1]==1 and a[2][0]==1:
            print("You Won")
            flag=0
            end='yes'


    
    
    if end=='n':        #To check if the computer won
        for i in range(3):
            if a[i][0]=='a' and a[i][1]=='a' and a[i][2]=='a':
                print("Computer Won")
                flag=0
                end='yes'
    
    
    
    if end=='n':
        for i in range(3):
            if a[0][i]=='a' and a[1][i]=='a' and a[2][i]=='a':
                print("Computer Won")
                flag=0
                end='yes'
    
    
    
    if end=='n':
        if a[0][0]=='a' and a[1][1]=='a' and a[2][2]=='a':
            print("Computer Won")
            flag=0
            end='yes'
    
    
    
    if end=='n':
        if a[0][2]=='a' and a[1][1]=='a' and a[2][0]=='a':
            print("Computer Won")
            flag=0
            end='yes'
    
    
    
    k+=1

    if flag==1 and end=='n':        #Random move
        s=[]
        for i in range(3):
            for j in range(3):
                if a[i][j]==0:
                    s+=[[i,j]]
        if len(s)==0:
            print("Draw")
            end='yes'
        else: 
            n=random.randint(0,len(s)-1)
            a[s[n][0]][s[n][1]]='a'



    for i in range(3):
        for j in range(3):
            if a[i][j]=='a':
                print('O',end=' ')
            elif a[i][j]==1:
                print('X',end=' ')
            else:
                print('*',end=' ')
        print('')
    print("\n\n")

else:
    pass


    


                
