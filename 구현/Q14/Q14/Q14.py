
import operator
from itertools import permutations
def solution(n, weak, dist):

    answer = 0
    """
    weak_dist={}
    for index,key in enumerate(weak):
        if index==len(weak)-1:
            weak_dist[index+1]=n-weak[index]+weak[0]
        else:
            weak_dist[index+1]=weak[index+1]-weak[index]
    
    
    #weak_dist=sorted(weak_dist.items(),key=lambda x:x[1])
    dist.sort(reverse=True)
    a=set()
    i=0
    count=0
    
    while(True):
        key=min(weak_dist,key=lambda x:weak_dist[x])
        while(True):
            if weak_dist[key]>dist[i]:
                i+=1
                print("+")
                break
            dist[i]=dist[i]-weak_dist[key]
            print(dist[i])
            a.add(key)
            a.add(key+1)
            print(a)
        if len(a)==len(weak):
                break
        
        
        for key,value in weak_dist.items():
            
               
        break
    """
    
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    # 투입된 수의 최소를 찾아야 하기 때문에 +1
    answer=len(dist)+1
    #처음 위치부터
    for start in range(length):
        #친구를 나열하는 모든 경우의 수
        for friends in list(permutations(dist,len(dist))):
            count=1
            #친구가 간 마지막 위치
            position=weak[start]+friends[count-1]
            #시작점부터 모든 취약지점(원 만큼만)
            for index in range(start,start+length):
                #만약 남았으면 한명 더하고
                if position<weak[index]:
                    count+=1
                    if count>len(dist):#투입 불가능
                        break
                    position=weak[index]+friends[count-1]
            answer=min(answer,count)#최솟값
    if answer>len(dist):
        return -1

    return answer