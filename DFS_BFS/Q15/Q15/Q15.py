from collections import deque

if __name__=="__main__":
    
    #처음 풀이 
    q=deque()

    n,m,k,x=map(int,input().split())
    arr=[]
    for i in range(m):
        arr.append(list(map(int,input().split())))

    visited=[0 for i in range(n)]

    q.append(x)
    visited[x]=1
    count=0
    next_count=1
    #k번만큼 도는데
    for _ in range(k):
        #이전 시간에 넣은 것들만 가져오기 위해서 개수를 세서 반복
        count=next_count
        next_count=0
        for _ in range(count):
            #큐에서 시작하는 점을 가져오고
            start=q.popleft()
            #저장된 도로를 하나씩 확인하면서
            for i in arr:
                #만약 시작점이 같고, 종료점을 방문하지 않은(최단거리) 도로라면
                if i[0]==start and visited[i[1]]==0:
                    #큐에 종료점을 넣고
                    q.append(i[1])
                    #방문했다고 표시
                    visited[i[1]]=1
                    #이후에 반복을 위해 count
                    next_count+=1
    if len(q)==0:
        print("-1")
    else:
        while q:
            inst=q.popleft()
            print(inst)
    #문제점 : 최단거리가 k 인 것을 구해야 하는데 k로 갈 수 있는 번호를 구해서 
    #최단 거리가 아닌 경우도 출력한다

    #해결: visited 배열을 사용해서 방문한 것(이미 큐에 넣었던 것)은 큐에 추가하지 않기