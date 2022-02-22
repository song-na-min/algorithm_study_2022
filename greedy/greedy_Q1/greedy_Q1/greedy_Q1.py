
import sys
#1.모험가길드

if __name__=="__main__":

    # input : N(배열의 크기) M(숫자가 더해지는 횟수) K(최대 덧셈 횟수?) 
    # 조건 : N과 M,K는 정수, 1<=N<=100,000,1<=M<=100,000,1<=K<=100,000 K<=M

    #먼저 N과 M,K를 입력받고, 공백으로 구분한다
	
	
    #첫번째줄 입력받기 => 위에서 입력받은 문자열 N과 M,K를 정수로 변환
    #또한 입력값이 조건에 적합한지 확인, 예외처리, 적합한 값을 입력받을 때 까지 반복

    while(True):
        try:
            N=input("N을 입력하세요:\n")
            n=int(N)
            
        except ValueError:#정수가 아닌 값 입력
            print("잘못된 값을 입력하였습니다.")
        else:
            break

    #두번째 줄을 입력받기, 숫자 리스트로 입력받음,리스트 개수 예외처리
    while(True):
        number=list(map(int,input().split()))
        if(len(number)==n):
            break
        else:
            print("리스트 개수가 맞지 않습니다.다시 입력해주세요!")

    result=0

    number.sort()

