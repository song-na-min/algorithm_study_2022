
import sys
#2.큰 수의 법칙

if __name__=="__main__":

    # input : N(배열의 크기) M(숫자가 더해지는 횟수) K(최대 덧셈 횟수?) 
    # 조건 : N과 M,K는 정수, 1<=N<=100,000,1<=M<=100,000,1<=K<=100,000 K<=M

    #먼저 N과 M,K를 입력받고, 공백으로 구분한다
	
	
    #첫번째줄 입력받기 => 위에서 입력받은 문자열 N과 M,K를 정수로 변환
    #또한 입력값이 조건에 적합한지 확인, 예외처리, 적합한 값을 입력받을 때 까지 반복

    while(True):
        try:
            N,M,K=input("N과 M,K를 입력하세요:\n").split()
            n=int(N)
            m=int(M)
            k=int(K)
            
        except ValueError:#정수가 아닌 값 입력
            print("잘못된 값을 입력하였습니다.")
        else:
            if(k<=m):#모든 조건에 만족하면 while문을 빠져나가고
                break
            print("잘못된 값을 입력하였습니다.")#k가 m보다 큰 경우 

    #두번째 줄을 입력받기, 숫자 리스트로 입력받음,리스트 개수 예외처리
    while(True):
        number=list(map(int,input().split()))
        if(len(number)==n):
            break
        else:
            print("리스트 개수가 맞지 않습니다.다시 입력해주세요!")

    result=0
    

    #가장 큰 값과 두번째로 큰 값 구하기
    #정렬하기 싫어서
    #가장 큰 값을 하나 찾고,그 index를 0으로 한 후
    max1=max(number)
    index=number.index(max1)
    number[index]=0
    #남은거중에서 가장 큰 값을 찾는다
    max2=max(number)

    #m번의 더하기를 할 때 max1을 k번 더하고 max2를 한번 더하는 것을 반복
    #이러한 경우 k+1 만큼이 반복되고 이 반복되는 횟수?를 a로 구한다
    a=m//(k+1)
    #b의 경우 k+1 덩어리들이 반복되고 남은 부분으로 max2가 마지막에 한번 더해지는 것이기
    #때문에 항상 max1이 곱해진다
    b=m%(k+1)

    #결과
    result=max1*(k*a+b)+max2*a
    # max1을 k번 더한것 과 max2 1개가 a번 반복되고, max1이 마지막에 b번 더해진다.

    print(result)