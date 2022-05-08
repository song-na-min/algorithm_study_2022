
from collections import deque
import copy

if __name__=="__main__":

    v=5
    indegree=[0]*(v+1)
    graph=[[]for _ in range(v+1)]
    time=[0]*(v+1)
    arr=[[10,-1],[10,1,-1],[4,1,-1],[4,3,1,-1],[3,3,-1]]
    for i in range(1,v+1):
        data=arr[i-1]
        time[i]=data[0]
        for x in data[1:-1]:
            indegree[i]+=1
            graph[x].append(i)
    print("graph:",end=" ")
    print(graph)

    print("indegree:",end=" ")
    print(indegree)

    def topology_sort():
        result=copy.deepcopy(time)
        print("result:",end=" ")
        print(result)
        q=deque()
        for i in range(1,v+1):
            if indegree[i]==0:
                q.append(i)
        while q:
            print("================")     

            now=q.popleft()
            print("pop:",end=" ")
            print(now)
            print("graph:",end=" ")
            print(graph[now])
            #result.append(now)
            for i in graph[now]:
                result[i]=max(result[i],result[now]+time[i])
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
            print("result:",end=" ")
            print(result)
            print("indegree:",end=" ")
            print(indegree)
            print("================")     
        for i in range(1,v+1):
            print(result[i])
    topology_sort()
    
