
import sys

#우선순위큐를 사용해서 get_smallest_node 대체
import heapq

def dijkstra(start,graph,distance):
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
    return distance
if __name__=="__main__":
    input=sys.stdin.readline
    INF=int(1e9)
    n,m=6,11
    start=1
    #n,m=map(int,input().split())
    #start node
    #start=int(input())
    graph=[[] for i in range(n+1)]
    #visited=[False]*(n+1)#visited또한 검사할 필요 없다
    
    #graph=[[],[(2,2),(3,5),(4,1)],[(3,3),(4,2)],[(2,3),(6,5)],[(3,3),(5,1)],[(3,1),(6,2)]]
    distance=[INF]*(n+1)
    
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
    
    result=dijkstra(start,graph,distance)
    print(result)