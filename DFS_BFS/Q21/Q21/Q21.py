from collections import deque

if __name__=="__main__":
    n,l,r=3,5,10

    arr=[[10,15,20],
          [20,30,25],
          [40,22,10]]

    dx=[-1,0,1,0]
    dy=[0,-1,0,1]

    def bfs(x,y,index):
        #united : 연합에 있는 배열의 x,y좌표 저장
        #=> 각 칸의 인구수를 바꿀 수 있도록
        united=[]
        united.append((x,y))
        q=deque()
        q.append((x,y))
        union[x][y]=index
        summary=arr[x][y]
        count=1

        while q:
            x,y=q.popleft()
            #상하좌우 검사
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                #만약 범위 내에있고, 연합이 정해지지 않았으면
                if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                    # 인구 차이가 l이상 r 이하이면 
                    if l<=abs(arr[nx][ny]-arr[x][y])<=r:
                        #연합에 추가
                        q.append((nx,ny))
                        #연합에 추가한 것을 배열에 반영(다음에 검사 안함)
                        union[nx][ny]=index
                        #합 추가
                        summary+=arr[nx][ny]
                        count+=1
                        united.append((nx,ny))
        #연합에 추가한 것들의 x,y좌표를 가져와서
        for i,j in united:
            #해당 칸의 인구수를 변경
            arr[i][j]=summary//count
        return count
    total_count=0
    while True:
        #초기화
        union=[[-1]*n for _ in range(n)]
        index=0
        for i in range(n):
            for j in range(n):
                # 아직 정해지 연합이 없는 경우 주변 확인
                if union[i][j]==-1:
                    bfs(i,j,index)
                    index+=1

        if index==n*n:
            break
        total_count+=1
    print(total_count)


    """
    union을 사용해서 연합이 있는지 확인하는 이유: 연합들을 다 검사하고,
    값을 변경한 후에 또 연합으로 묶이는 것을 방지하기 위해
    """
