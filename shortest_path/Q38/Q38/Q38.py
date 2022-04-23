

if __name__=="__main__":
    INF=int(1e9)
    n=int(input())
    m=int(input())

    graph=[[INF]*(n+1) for _ in range(n+1)]
    
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a==b:
                graph[a][b]=0
    arr=[
        [1,5],
        [3,4],
        [4,2],
        [4,6],
        [5,2],
        [5,4]
    ]
    better_or_not=[
        [],
        [],
        [],
        [],
        [],
[],       
[]]
    for edge in arr:
        a,b,c=edge[0],edge[1],1
        graph[a][b]=c
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
    #print(graph)

    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                continue
            if graph[i][j]!=INF:
                better_or_not[i].append(j)
            if graph[j][i]!=INF:
                better_or_not[i].append(j)
    #print(better_or_not)
    for index,value in enumerate(better_or_not):
        #print(value)
        if len(value)==(n-1):
            print(index)
    """
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a][b]=min(c,graph[a][b])
    """
    