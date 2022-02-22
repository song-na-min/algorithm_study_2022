
import sys
#2.큰 수의 법칙

if __name__=="__main__":



    while(True):
        try:
            N,M=input("N과 M을 입력하세요:\n").split()
            n=int(N)
            m=int(M)
            
        except ValueError:#정수가 아닌 값 입력
            print("잘못된 값을 입력하였습니다.")
        else:
            break

    #두번째 줄을 입력받기, 숫자 리스트로 입력받음,리스트 개수 예외처리
    while(True):
        number=list(map(int,input().split()))
        if(len(number)==n and max(number)==m):
            break
        else:
            print("리스트 개수가 맞지 않습니다.다시 입력해주세요!")
    count_list={}

    for i in number:
        try:count_list[i]=count_list[i]+1
        except:count_list[i]=1
    print(count_list)

    #이후 값?을 계산할 숫자
    minus=0
    result=0

    for key,value in count_list.items():
        minus=minus+value
        #print((n-minus)*value)
        result=result+(n-minus)*value
        
        
    print(result)
        


    result=0