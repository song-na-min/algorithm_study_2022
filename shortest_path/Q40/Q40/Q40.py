import heapq
if __name__=="__main__":
    INF=int(1e9)
    n=6
    m=7
    graph=[[] for _ in range(n+1)]
    arr=[[3,6],
         [4,3],
         [3,2],
         [1,3],
         [1,2],
         [2,4],
         [5,2]]
    start=1
    distance=[INF]*(n+1)
    for t in arr:
        a,b=t[0],t[1]
        graph[a].append((b,1))
        graph[b].append((a,1))
    
    def dijkstra(start):
        q=[]

        heapq.heappush(q,(0,start))
        distance[start]=0

        while q:
            dist,now=heapq.heappop(q)
            #이미 처리된 노드는 넘어가기
            if distance[now]<dist:
                continue
            for i in graph[now]:
                #cost= 시작점-선택노드 거리 + 선택노드 - 도착노드 거리
                cost=dist+i[1]
                #단 이전에 갱신한, 다른 길로 가는것 보다 빠르면 갱신하고,큐에 넣기
                if cost<distance[i[0]]:
                    distance[i[0]]=cost
                    heapq.heappush(q,(cost,i[0]))
    dijkstra(start)

    max_node=0
    max_distance=0
    result=[]

    for i in range(1,n+1):
        if max_distance<distance[i]:
            max_node=i
            max_distance=distance[i]
            result=[max_node]
        elif max_distance==distance[i]:
            result.append(i)
    print(max_node,max_distance,len(result))






    """
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a==b:
                graph[a][b]=0
    for k in arr:
        a,b=k[0],k[1]
        graph[a][b]=1
    
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
    for i in graph:
        for j in range(1,n+1):
            if i[j]==INF:
                print("0",end=" ")
            else:
                print(i[j],end=" ")
        print("")
    max=0
    max_index=0
    count=0
    for j in range(1,n+1):
        if graph[1][j]>max and graph[1][j]!=INF:
            max_index=j
            max=graph[1][j]

    print(max_index,max,graph.count(max))
    #플로이드 알고리즘을 사용하면 max는 구할 수 있지만 같은 개수는 구할 수 없다
    """