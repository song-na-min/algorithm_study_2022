
#결합도 응집도
def find(parent,x):
    if parent[x]!=x:
        return find(parent,parent[x])
    return x

def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

if __name__=="__main__":
    #v,e=map(int,input().split())
    v,e=6,4

    parent=[0]*(v+1)
    for i in range(1,v+1):
        parent[i]=i
    e=[[1,4],[2,3],[2,4],[5,6]]
    for i in e:
        a,b=i
        union(parent,a,b)
    print("부모 테이블:",end=" ")
    for i in range(1,v+1):
        print(parent[i],end=" ")
    print()
    print("각 원소가 속한 집합:",end=" ")
    for i in range(1,v+1):
        print(find(parent,i),end=" ")
    print()
    print("부모 테이블:",end=" ")
    for i in range(1,v+1):
        print(parent[i],end=" ")