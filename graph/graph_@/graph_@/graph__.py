
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
    n,m=7,8
    parent=[0]*(n+1)
    
    for i in range(0,n+1):
        parent[i]=i
    arr=[[0,1,3],
         [1,1,7],
         [0,7,6],
         [1,7,1],
         [0,3,7],
         [0,4,2],
         [0,1,1],
         [1,1,1]]
    for oper in arr:
        if oper[0]==0:
            union(parent,oper[1],oper[2])
        elif oper[0]==1:
            if find(parent,oper[1])==find(parent,oper[2]):
                print("YES")
            else:
                print("No")