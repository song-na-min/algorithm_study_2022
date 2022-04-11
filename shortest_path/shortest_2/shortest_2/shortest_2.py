import sys

if __name__=="__main__":

    n,m=4,2
    INF=int(1e9)
    start=1
    graph=[[INF]*(n+1) for _ in range(n+1)]
    
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a==b:
                graph[a][b]=0
    for _ in range(m):
        a,b=map(int,input().split())
        graph[a][b]=1
        graph[b][a]=1
    
    x,k=3,4
    for t in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b]=min(graph[a][b],graph[a][t]+graph[t][b])
    one_k=graph[1][k]
    k_x=graph[k][x]
    #print(graph)
    if one_k==INF or k_x==INF:
        print("-1")
    else:
        print(one_k+k_x)