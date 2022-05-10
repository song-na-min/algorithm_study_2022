from collections import deque
if __name__=="__main__":

    #n=5
    #last=[5,4,3,2,1]
    #m=2
    #switches=[(2,4),(3,4)]
    n=3
    last=[2,3,1]
    m=0
    switches=[]
    indegree=[0]*(n+1)
    graph=[[] for _ in range(n+1)]
    for rank in range(1,n+1):
        indegree[last[rank-1]]=rank-1
        graph[last[rank-1]].extend(last[rank:])
    #print(graph)
    #print(indegree)

    for switch in switches:
        
        i,j=last.index(switch[0]),last.index(switch[1])
        #print(i,j)
        a=last[i] if i>j else last[j]
        b=last[j] if i>j else last[i]
        #print(a,b)
        indegree[b]+=1
        indegree[a]-=1
        graph[a].append(b)
        graph[b].remove(a)
    #print(graph)
    #print(indegree)
    certain=True
    def topology_sort():
        result=[]
        q=deque()
        for i in range(1,n+1):
            if indegree[i]==0:
                q.append(i)
        while q:
            if len(q)>=2:
                certain=False
                break
            now=q.popleft()
            result.append(now)
            for i in graph[now]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        if len(result)!=n:
            print("impossible")
        else:
            for i in result:
                print(i,end=" ")
    topology_sort()
    if certain==False:
        print("?")
