
#3. 문자열 뒤집기

if __name__=="__main__":

    s=input("S을 입력하세요:\n")

    int_list=list(map(int,str(s)))

    count=[0,0]

    #초기화 : 처음 시작하는 수를 count한다
    count[int_list[0]]=1
    #print(count)

    for index,value in enumerate(int_list):
        
        if index == len(int_list)-1:
            break
        
        diff = value - int_list[index+1]
        #print(count)
        
        #0에서 1로 변할 때 1이 count
        if diff==-1:
            count[1]=count[1]+1
        #1에서 0으로 변할 때 0이 count
        elif diff==1:
            count[0]=count[0]+1
    print(count.index(min(count)))