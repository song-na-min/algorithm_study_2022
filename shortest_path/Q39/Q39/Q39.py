import heapq

if __name__=="__main__":
    INF=int(1e9)
    n=int(input())
    graph=[[3,7,2,0,1],
         [2,8,0,9,1],
         [1,2,1,8,1],
         [9,8,9,2,0],
         [3,6,5,1,5]]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    x,y=0,0
    distance=[[INF]*n for _ in range(n)]
    q=[(graph[x][y],x,y)]


    while q:
        dist,x,y=heapq.heappop(q)
        if distance[x][y]<dist:
            continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            cost=dist+graph[nx][ny]
            if cost<distance[nx][ny]:
                distance[nx][ny]=cost
                heapq.heappush(q,(cost,nx,ny))
    print(distance[n-1][n-1])
    """
    for i in range(1,n):
        arr[i][0]+=arr[i-1][0]
        arr[0][i]+=arr[0][i-1]
    for i in range(1,n):
        for j in range(1,n):
            arr[i][j]+=min(arr[i-1][j],arr[i][j-1])
    print(arr)
    print(arr[n-1][n-1])
    
    arr=[[5,5,4],
         [3,9,1],
         [3,2,7]]
    """
    
