import numpy

#2차원 배열 회전함수
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

#lock의 원래부분의 값이 다 1인지 확인
def check(new_lock):
    for i in range(n,n*2):
        for j in range(n,n*2):
            if new_lock[i][j]!=1:
                return False
    return True


def solution(key, lock):
    answer = True
    global n 
    n= len(lock)
    m=len(key)
    #lock 초기화
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j]=lock[i][j]
    
    #90도씩 4번 돌려본다
    for rot in range(4):
        key=rotate_90(key)
        #왼쪽 위부터
        for x in range(n*2):
            for y in range(n*2):
                #key의 값을 lock에 더해보고
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                #만약 lock의 중간부분(원래 lock 부분)이 다 1이면 True
                if check(new_lock)==True:
                    return True
                #넣었던 key를 뺀다
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    #만약 4번 돌려서 다 확인했는데도 없으면 False
    return False
