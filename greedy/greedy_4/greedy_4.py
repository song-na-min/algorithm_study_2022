

if __name__=="__main__":

    # input : N K
    # 조건 : N과 K는 정수, 1<N<=100,000,1<K<=100,000, N>=K

    #먼저 N과 K를 입력받고, 공백으로 구분한다
	
	
    #위에서 입력받은 문자열 N과 K를 정수로 변환
    #또한 입력값이 조건에 적합한지 확인, 예외처리, 적합한 값을 입력받을 때 까지 반복
    while(True):
        try:
            N,K=input("N과 K를 입력하세요:\n").split()
            n=int(N)
            k=int(K)
            
        except ValueError:#정수가 아닌 값 입력
            print("잘못된 값을 입력하였습니다.")
        else:
            if(n>=k):#모든 조건에 만족하면 while문을 빠져나가고
                break
            print("잘못된 값을 입력하였습니다.")#k가 n보다 큰 경우 


    count=0

    while(n!=1):#n이 1이 될 때 까지
        if(n%k==0):#n이 k로 나누어떨어지면 우선적으로 나눈다
            n=n/k
            count=count+1
        else:#나누어떨어지지 않으면 1을 뺀다
            n=n-1
            count=count+1
    print(count)#결과: N이 1이 될때까지 실행되는 과정의 최소값
	
	
