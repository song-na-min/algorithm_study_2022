
import sys
#4.만들 수 없는 금액

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
    while(True):
        number=list(map(int,input().split()))
        if(len(number)==n):
            break
        else:
            print("리스트 개수가 맞지 않습니다.다시 입력해주세요!")

    result=0
    
    #sort
    index=0
    number.sort()
    sum=0

    if number[0]!=1:
        result=1
    else:
        #초반 수
        sum=sum+number[0]
        while(number[index+1]-number[index]<2):
            sum=sum+number[index+1]          
            index=index+1
        index=index+1
        while(result==0):
            """
            print(index)
            print("sum : {}".format(sum))  
            print("=======================")
            """
            if len(number)==index:
                result=sum+1
                break

            #if (sum+number[index]+1)<number[index+1]:
            if sum+2<=number[index]:
                result=sum+1
                break
            else:
                sum=sum+number[index]
                index=index+1
             
            
            
    

    print(result)