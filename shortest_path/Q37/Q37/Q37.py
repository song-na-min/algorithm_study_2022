
if __name__=="__main__":
    INF=int(1e9)
    n=int(input())
    m=int(input())

    graph=[[INF]*(n+1) for _ in range(n+1)]
    
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a==b:
                graph[a][b]=0
    arr=[[1,2,2],
         [1,3,3],
         [1,4,1],
         [1,5,10],
         [2,4,2],
         [3,4,1],
         [3,5,1],
         [4,5,3],
         [3,5,10],
         [3,1,8],
         [1,4,2],
         [5,1,7],
         [3,4,2],
         [5,2,4]
    ]
    for edge in arr:
        a,b,c=edge[0],edge[1],edge[2]
        graph[a][b]=min(c,graph[a][b])
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
    #print(graph)
    for i in graph:
        for j in range(1,n+1):
            if i[j]==INF:
                print("0",end=" ")
            else:
                print(i[j],end=" ")
        print("")

    """
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a][b]=min(c,graph[a][b])
    """
    