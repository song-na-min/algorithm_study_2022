

def find(parent,x):
    if parent[x]!=x:
        parent[x]= find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

if __name__=="__main__":
    
    g=4
    parent=[0]*(g+1)
    for i in range(1,g+1):
        parent[i]=i
    p=[4,1,1]
    result=0
    for to in p:
        data=find(parent,to)
        if data==0:
            break
        union(parent,data,data-1)
        result+=1
    print(result)
