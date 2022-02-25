
if __name__=="__main__":
    while(True):
        try:
            N=input("N을 입력하세요:\n")
            n=int(N)
            
        except ValueError:#정수가 아닌 값 입력
            print("잘못된 값을 입력하였습니다.")
        else:
            break

    #두번째 줄을 입력받기, 숫자 리스트로 입력받음,리스트 개수 예외처리
    move=input().split()
    #print(move)
       
    to=['L','R','U','D']
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]

    x=1
    y=1
    for A in move:
        index=to.index(A)
        if (0<x+dx[index]<=5) and (0<y+dy[index]<=5):
            x=x+dx[index]
            y=y+dy[index]
           
    print(x,",",y)
