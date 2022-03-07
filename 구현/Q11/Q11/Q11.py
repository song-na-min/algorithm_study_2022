from collections import deque
def turn(direction,c):
    if c=="L":
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
    return direction
if __name__=="__main__":

    n=int(input())
    k=int(input())
    m=[[0]*(n+2) for _ in range(n+2)]
    for i in range(k):
        x,y=map(int,input().split())
        m[x][y]=1
    l=int(input())
    dist=[]
    for _ in range(l):
        t,d=input().split()
        dist.append((int(t),d))
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    
    x,y=1,1
    m[x][y]=2
    direction=0
    time=0
    q=[(x,y)]
    index=0

    while True:
        nx=x+dx[direction]
        ny=y+dy[direction]

        if 1<=nx<=n and 1<=ny<=n and m[nx][ny]!=2:
            
            m[nx][ny]=2
            q.append((nx,ny))

            if m[nx][ny]==0:
                px,py=q.pop(0)
                data[px][py]=0
     
        else:
            time+=1
            break
        x,y=nx,ny
        time+=1
        if index<1 and time==dist[index][0]:
            direction=turn(direction,dist[index][1])
            index+=1

    print(time)
