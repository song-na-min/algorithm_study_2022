from itertools import combinations
from collections import deque
if __name__=="__main__":
    '''
    n,m=7,7
    arr=[[2,0,0,0,1,1,0],
         [0,0,1,0,1,2,0],
         [0,1,1,0,1,0,0],
         [0,1,0,0,0,0,0],
         [0,0,0,0,0,1,1],
         [0,1,0,0,0,0,0],
         [0,1,0,0,0,0,0]]
    '''

    #input을 할 때 arr과 arr_new를 동시에 입력받기(같도록) 
    #이유: arr=[]을 선언할 경우 범위 오류
    n,m=4,6
    arr=[[0,0,0,0,0,0],
         [1,0,0,0,0,2],
         [1,1,1,0,0,2],
         [0,0,0,0,0,2],
        ]
    arr_new=[[0,0,0,0,0,0],
         [1,0,0,0,0,2],
         [1,1,1,0,0,2],
         [0,0,0,0,0,2],
        ]
     
    
    count_start_2=0
    count_start_1=0
    list_0=[]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    #print(n,m)
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                count_start_1+=1
            elif arr[i][j]==2:
                count_start_2+=1
            else:
                list_0.append((i,j))

    min_2=m*n
    #combinati=[[(1,0),(0,1),(3,5)]]
    #for combi in combinations(list_0,3):
    
    def bfs(startx,starty):
        queue=deque()
        queue.append((startx,starty))
        count=0
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=m:
                    continue
                if arr_new[nx][ny]==1:
                    continue
                if arr_new[nx][ny]==0:
                    arr_new[nx][ny]=2
                    count += 1
                    #print(nx,ny)
                    queue.append((nx,ny))
                    #print(count)
        return count
    for combi in combinations(list_0,3):
        #print(combi[0])
        #초기화
        count_2=0
        for x in range(n):
            for y in range(m):
                arr_new[x][y]=arr[x][y]

        arr_new[combi[0][0]][combi[0][1]]=1
        arr_new[combi[1][0]][combi[1][1]]=1
        arr_new[combi[2][0]][combi[2][1]]=1
        #print(arr_new)

        for k in range(n):
            for p in range(m):
                if arr_new[k][p]==2:
                    count_2 += bfs(k,p)
                    #print(count_2)
        if min_2>count_2:
            min_2=count_2
    #print(arr_new)
    #n*m-처음1의 개수-처음2의 개수- 추가된 2의 개수- 추가된 1의 개수(3)=0의 개수
    print(n*m-count_start_1-count_start_2-min_2-3)

