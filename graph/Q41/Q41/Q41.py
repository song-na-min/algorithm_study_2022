
def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]
def union_parent(parent,a,b):
  a=find_parent(parent,a)
  b=find_parent(parent,b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b



if __name__=="__main__":
    n=5
    m=4
    graph=[[0,1,0,1,1],[1,0,1,1,0],[0,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0]]
    path=[2,3,4,3]
    parent=[0]*(n+1)
    for i in range(1,n+1):
        parent[i]=i
    for i in range(n):
        for j in range(i):
            if graph[i][j]==1:
                #print(i+1,j+1)
                union_parent(parent,i+1,j+1)
    #print("각 원소가 속한 집합:",end=" ")
    root=find_parent(parent,path[0])
    result=True
    for i in path:
        if root!=find_parent(parent,i):
            result=False
            break
    if result==True:
        print("YES")
    else:
        print("NO")