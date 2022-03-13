
from collections import deque

if __name__=="__main__":

    #input
    #n,m=map(int,input().split())
    #arr=[list(map(int,input())) for _ in range(n)]
    n=15
    m=14
    arr=[[0,0,0,0,0,1,1,1,1,0,0,0,0,0],
         [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
         [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
         [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
         [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
         [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
         [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
         [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
         [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
         [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
         [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
         [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
         [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
         ]

    #dfs를 이용한 풀이
    def dfs(x,y):
        if x<0 or x>=n or y<0 or y>=m:
            return False
        if arr[x][y]==0:#만약 0이면
            arr[x][y]=1#해당 칸을 1로 바꾼 후
            dfs(x-1,y)
            dfs(x,y-1)
            dfs(x,y+1)
            dfs(x+1,y)#네 방향으로 재귀함수
            return True
        return False
    result=0

    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                result+=1   

    print(result)

    """
    #bfs를 이용한 풀이

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    def bfs(startx,starty):
        queue=deque()
        queue.append((startx,starty))
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if arr[nx][ny]==1:
                    continue
                if arr[nx][ny]==0:
                    arr[nx][ny]=1
                    queue.append((nx,ny))
    count=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                bfs(i,j)
                count+=1

    print(count)
    """
