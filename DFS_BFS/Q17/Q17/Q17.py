    
import queue
from collections import deque


if __name__=="__main__":
    
    #queue에 넣을 클래스
    #https://lovedh.tistory.com/entry/Python-Priority-Queue%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-%EA%B0%9D%EC%B2%B4-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0
    #우선순위 큐로 정렬하기 위해
    class Data:
        def __init__(self,x,y,value):
            self.x=x
            self.y=y
            self.value=value
        def __lt__(self,other): 
            return self.value<other.value

    n=3
    k=3
    arr=[[1,0,2],
         [0,0,0],
         [3,0,0]]
    s,x,y=1,2,2

    q=deque()
    pri_queue=queue.PriorityQueue()

    #상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    #처음 k개의 바이러스를 x,y,value로 우선순위 큐에 저장
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                pri_queue.put(Data(i,j,arr[i][j]))

    #저장한 우선순위 큐를 그냥 큐에 저장
    #시작할 때 queue를 정렬하기 위해
    while not pri_queue.empty():
        inst=pri_queue.get()
        #print(inst.x,inst.y,inst.value)
        q.append(Data(inst.x,inst.y,inst.value))


    count=k
    #s초만큼 반복
    for _ in range(s):
        #이전 시간에 넣은 것들만 가져오기 위해서 개수를 세서 반복
        k=count
        count=0
        #print(k)
        for _ in range(k):
            virus=q.popleft()
            #print(virus.value,virus.x,virus.y)
            #상하좌우
            for i in range(4):
                nx=virus.x+dx[i]
                ny=virus.y+dy[i]
                #print(nx,ny)
                #범위를 벗어나는 경우
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    continue
                #0일 때
                if arr[nx][ny]==0:
                    #print(arr[nx][ny])
                    #해당 위치의 값을 바꾸고
                    arr[nx][ny]=virus.value
                    #print(arr[nx][ny])
                    #큐에 위치와 값 insert
                    q.append(Data(nx,ny,virus.value))
                    count+=1
                    #print(arr)

    #print(arr)
    print(arr[x-1][y-1])

    #priority queue를 쓴 이유는 작은 바이러스가 우선하기 때문에 작은거부터 확산시키기 위해
    #count는 새로 추가한 값과 기존 값을 분리하기 위해