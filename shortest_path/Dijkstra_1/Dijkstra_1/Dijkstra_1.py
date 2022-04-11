import sys

#방문하지 않은 노드 중 최단거리가 짧은 노드 반환
def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start,graph,visited,distance):
    #시작점 초기화
    distance[start]=0
    visited[start]=True
    #시작점에서 출발하는 간선들로 distance 초기화
    for j in graph[start]:
        distance[j[0]]=j[1]

    #시작점 제외 모든 노드들
    for i in range(n-1):
        #방문하지 않고 거리가 가장 짧은 노드 선택
        now = get_smallest_node()
        visited[now]=True
        # 선택한 노드에서 출발하는 간선을 보고 갱신
        for j in graph[now]:
            #cost= 시작점-선택노드 거리 + 선택노드 - 도착노드 거리
            cost=distance[now]+j[1]
            #단 이전에 갱신한, 다른 길로 가는것 보다 빠르면 갱신하도록
            if cost<distance[j[0]]:
                distance[j[0]]=cost
    return distance
if __name__=="__main__":
    input=sys.stdin.readline
    INF=int(1e9)

    n,m=map(int,input().split())
    #start node
    start=int(input())
    graph=[[] for i in range(n+1)]
    visited=[False]*(n+1)
    distance=[INF]*(n+1)

    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))

    result=dijkstra(start,graph,visited,distance)
    print(result)