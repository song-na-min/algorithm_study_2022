
#숫자 카드 게임

if __name__=="__main__":

    # input : N(행) M(열)
    # 조건 : N과 M는 정수, 1<=N<=100,000,1<=M<=100,000

    #먼저 N과 M를 입력받고, 공백으로 구분한다
	
	
    #첫번째줄 입력받기 => 위에서 입력받은 문자열 N과 M를 정수로 변환
    #또한 입력값이 조건에 적합한지 확인, 예외처리, 적합한 값을 입력받을 때 까지 반복

    while(True):
        try:
            N,M=input("N과 M를 입력하세요:\n").split()
            n=int(N)
            m=int(M)
            
        except ValueError:#정수가 아닌 값 입력
            print("잘못된 값을 입력하였습니다.")
        else:
            break
    #두번째 줄을 입력받기, 숫자 리스트로 입력받음
    number=[[int(x) for x in input().split()]for y in range(n)]

    
    min_list=[]

    #저장한 2차원 배열에서 한 행씩 추출,해당 행에서 최소값을 list에 저장
    for i in number:
        #print(min(i))
        min_list.append(min(i))

    #print(min_list)

    #print("======")
    #최소값들을 모아놓은 list에서 가장 큰 원소
    print(max(min_list))