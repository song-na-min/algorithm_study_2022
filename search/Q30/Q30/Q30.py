
"""
#초반 풀이 : 각 단어들을 쿼리랑 비교해서 확인하는 코드 작성
#하지만 특정 위치의 단어는 비교하지 않는 문제 발생
#또 맞는 경우 어차피 다 읽어야 하기 때문에 binary search를 사용할 필요가 없다
def search(word,query,start,end):
    #확인할 단어, 쿼리(알파벳만),시작위치,끝위치
    #중심을 기준으로 오른쪽,왼쪽을 번갈아가면서 비교하려고 함
    print(word,query)
    start_query,end_query=start,end
    center=(start+end)//2
    all=[0,0]
    while True:
        if all[0]==1 and all[1]==1:
            break
        mid=(start+end)//2
        print(mid)
        #print(all)
        if word[mid]!=query[mid]:
            print("No")
            return False
        elif mid<center and mid>-1:
            if start_query==mid:
                #print("start")
                all[0]=1
            start=mid+1
        elif mid>=center:
            if end_query==mid:
                #print("end")
                all[1]=1
            end=mid-1
    print("YES")
    return True  
"""
"""
    #쿼리랑 단어 길이 확인하고 함수로 넘어가자
    for query in queries:
        count=0
        full_length=len(query)
        start_diff=query.find("?")
        if start_diff==0:
            start=query.count("?")
            end=full_length-1
        else:
            start=0
            end=full_length-1-query.count("?")
        for word in words:
            if len(word)==full_length:
                if search(word,query,start,end):
                    count+=1
                answer.append(count)
"""

#답지
#각 단어의 길이별로 리스트를 나누고 정렬한 후 쿼리의 길이를 보고 맞는 리스트를 확인
# bisect : https://heytech.tistory.com/79
from bisect import bisect_left,bisect_right
def count_by_range(a,left_value,right_value):
    right_index=bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)
    return right_index-left_index
array=[[] for _ in range(10001)]
reversed_array=[[] for _ in range(10001)]
def solution(words, queries):
    
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
        
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
    for q in queries:
        if q[0]!="?":
            res=count_by_range(array[len(q)],q.replace("?","a"),q.replace("?","z"))
        else:
            res=count_by_range(reversed_array[len(q)],q[::-1].replace("?","a"),q[::-1].replace("?","z"))
        answer.append(res)
                
    
    return answer