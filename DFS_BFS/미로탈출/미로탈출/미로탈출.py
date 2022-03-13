from collections import deque

if __name__=="__main__":
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input())))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    x,y=0,0
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if arr[nx][ny]==0:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny]=arr[x][y]+1
                queue.append((nx,ny))
    print(arr[n-1][m-1])
    #print(arr)
