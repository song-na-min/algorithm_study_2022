
from itertools import combinations
from collections import deque

if __name__=="__main__":
   
    #input을 할 때 arr과 arr_new를 동시에 입력받기(같도록) 
    #이유: arr=[]을 선언할 경우 범위 오류
    ## T:2, X:0, 1:S
    """
    n,m=5,5
    
    def print_Array(arr):
        print("---------")
        for i in arr:
            print(i)
    arr=[[0,1,0,0,2],
         [2,0,1,0,0],
         [0,0,0,0,0],
         [0,2,0,0,0],
         [0,0,2,0,0]
        ]
    arr_new=[[0,1,0,0,2],
         [2,0,1,0,0],
         [0,0,0,0,0],
         [0,2,0,0,0],
         [0,0,2,0,0]
        ]
    """
    n,m=4,4
    arr=[[1,1,1,2],
         [0,0,0,0],
         [0,0,0,0],
         [2,2,2,0]
        ]
    arr_new=[[1,1,1,2],
         [0,0,0,0],
         [0,0,0,0],
         [2,2,2,0]
        ]
    
    list_0=[]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    list_2=[]
    #print(n,m)
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                list_0.append((i,j))
            if arr[i][j]==2:
                list_2.append((i,j))
    #print(list_0)
    def bfs():
        #모든 2에서 출발해서
        for T in list_2:
            x=T[0]
            y=T[1]
            #상하좌우로 끝까지 검사
            for i in range(4):
                #print_Array(arr_new)
                for k in range(n):
                    nx=x+dx[i]*k
                    ny=y+dy[i]*k
                    if nx<0 or ny<0 or nx>=n or ny>=m:
                        break
                #print(nx,ny,arr_new[nx][ny])
                    if arr_new[nx][ny]==3:#장애물
                        break
                    if arr_new[nx][ny]==0:#빈 공간
                        arr_new[nx][ny]=2
           
                    if arr_new[nx][ny]==1:#S인 경우 no
                        #print(nx,ny)
                        #print("NO")
                        return "NO"
        return "YES"
        
        
    result="NO"
    #list_0=[(0,3),(1,1),(2,2)]
    for combi in combinations(list_0,3):
        #print(combi[0])
        #초기화
        result="YES"
        for x in range(n):
            for y in range(m):
                arr_new[x][y]=arr[x][y]

        arr_new[combi[0][0]][combi[0][1]]=3
        arr_new[combi[1][0]][combi[1][1]]=3
        arr_new[combi[2][0]][combi[2][1]]=3
        #print(arr_new)

        result=bfs()
                
        if result=="YES":#만약 가능한 경우가 있으면 종료
            print_Array(arr_new)
            break
        
    if result=="YES":
        print("YES")
    else:
        print("No")

        