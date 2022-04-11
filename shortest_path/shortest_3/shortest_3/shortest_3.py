
import sys
import heapq
def dijkstra(start,graph,distance):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return distance
if __name__=="__main__":
    n,m,c=3,2,1
    INF=int(1e9)
    graph=[[] for _ in range(n+1)]
    distance=[INF]*(n+1)

    for _ in range(m):
        x,y,z=map(int,input().split())
        graph[x].append((y,z))
        
    result=dijkstra(c,graph,distance)
    count=0
    time=0
    for i in result:
        if i!=INF:
            count+=1
            time=max(time,i)
    print(count-1,time)