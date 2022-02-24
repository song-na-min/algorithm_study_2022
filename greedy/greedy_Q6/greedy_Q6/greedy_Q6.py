"""
import numpy as np
if __name__=="__main__":
    food_times=[3,1,2]
    k=5
    answer = 0
    
    while (k>=len(food_times)):
        k=k-np.min(ffood_times[food_times!=0])*len(food_times)
        print(k)
"""

"""
    answer = -1
    p=0
    len_food=len(food_times)
    while (k>=len_food):
        #print(len_food,k)
        m=min(food_times,key=lambda x:x>p)
        #print(m)
        k=k-m*len_food
        len_food=len_food-1
        #print(len_food,k)
        p=p+m
    k=k+2
    i=0
    while(k!=0 and i<len(food_times)):
        if(food_times[i]>p):
            k=k-1
            answer=i+1
            
    print(answer)
    return answer
"""
import numpy as np
import sys
import heapq

def solution(food_times, k):
    if(sum(food_times)<=k):
        answer=-1
    q=[]
    len_food=len(food_times)
    for i in range(len_food):
        heapq.heappush(q,(food_times[i],i+1))
    pre=0
    sum_value=0
    while (k>=sum_value+len_food*(q[0][0]-pre)):
       # print(m)
        m=heapq.heappop(q)[0]
        sum_value+=(m-pre)*len_food
        len_food=len_food-1
        #print(len_food,k)
        pre=m
        
        
    result=sorted(q,key=lambda x:x[1])
    answer=result[(k-sum_value)%len_food][1]
            
    print(answer)
    return answer