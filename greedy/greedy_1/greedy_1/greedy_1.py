
# 거스름돈
# input: N ,조건:정수,10의 배수
# 500,100,50,10원으로 거슬러줄 수 있는 동전의 최소 개수

if __name__=="__main__":
    
    #입력
    #조건 예외처리
    while(True):
        try:
            N=int(input("거슬러줘야할 돈을 입력하세요"))
        except ValueError:
            print("잘못된 값을 입력하였습니다.")
        else:
            if(N%10==0):
                break
            print("잘못된 값을 입력하였습니다.")


    #count 초기화
    count=0

    # 화폐단위를 배열로 저장
    a=[500,100,50,10]

    for num in a:#화페단위를 큰거부터 하나씩
        count=count+N//num #N과 num의 정수 몫을 count
        N=N%num #나머지를 N으로

    

    print(count)
