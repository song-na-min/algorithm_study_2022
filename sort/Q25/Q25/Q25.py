
def solution(N, stages):
    answer = []
    #거꾸로 정렬
    stages=sorted(stages,reverse=True)
    #print(stages)
    #초기화
    fail_rate_list=[]
    #단 모두 성공한? 값이 N+1인 것도 포함하기 위해 크기 N+2로
    fail=[0 for _ in range(N+2)]
    do=[0 for _ in range(N+2)]

    
    for index,value in enumerate(stages):
        #해당 스테이지에서 실패=> 실패+1
        fail[value]+=1
        #해당 스테이지의 index+1까지 도전한 사람
        do[value]=index+1
        """ex) [6,5,4,3,3,2,2,2,1]에서 3까지 도전한 사람은 5명
                ->3인 마지막 index+1=4+1
        """
    #실패율 계산하고 (index,실패율)리스트에 추가
    for j in range(1,N+1):
        #단 0으로 나누는 것은 오류이므로 확인하기!
        if do[j]!=0:
            fail_rate_list.append((j,fail[j]/do[j]))
        else:
            fail_rate_list.append((j,0))
    #print(fail_rate_list)
    #실패율로 거꾸로 정렬
    fail_rate_list.sort(key= lambda x:x[1],reverse=True)
    #정렬된 리스트를 순서대로 인덱스를 넣기
    for i in fail_rate_list:
        answer.append(i[0])
    return answer

"""
#solution
    length=len(stages)

    for i in range(1,N+1):
        count=stages.count(i)

        if length==0:
            fail=0
        else:
            fail=count/length
        answer.append((i,fail))
        length-=count
        
    return answer
"""