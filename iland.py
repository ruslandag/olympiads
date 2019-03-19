n=int(input())
m=int(input())

pole=[]
for i in range(n):
    pole.append([0]*m)

for i in range(n):
    stroka=input()
    for j in range(len(stroka)):
        if stroka[j]=='#':
            pole[i][j]=1
for i in range(n):
    for j in range(m):
        if pole[i][j]==1:
            if pole[i-1][j]==0:
                pole[i-1][j]=2
            if pole[i-1][j+1]==0:
                pole[i-1][j+1]=2
            if pole[i][j+1]==0:
                pole[i][j+1]=2
            if pole[i+1][j+1]==0:
                pole[i+1][j+1]=2
            if pole[i+1][j]==0:
                pole[i+1][j]=2
            if pole[i+1][j-1]==0:
                pole[i+1][j-1]=2
            if pole[i-1][j-1]==0:
                pole[i-1][j-1]=2
            if pole[i][j-1]==0:
                pole[i][j-1]=2

for i in range(n):
    for j in range(m):
        if pole[i][j]==2:
            x=i
            y=j
while (pole[x][y]==2):            
    print(x,y)
    if pole[x-1][y]==2:
        x-=1
        pole[x-1][y]=3
    elif pole[x][y+1]==2:
        y+=1
        pole[x][y+1]=3
    elif pole[x+1][y]==2:
        x+=1
        pole[x+1][y]=3
    elif pole[x][y-1]==2:
        y-=1
        pole[x][y-1]=3