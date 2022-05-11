
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

def kruskal(edges,v,e):
  #edges=make_edges(points)
  #v=len(points)
  parent=[0]*(v+1)
  result=0
  for i in range(1,v+1):
    parent[i]=i
  edges.sort()
  total=0
  for edge in edges:
    cost,a,b=edge
    #전체 비용
    total+=cost
    if find_parent(parent,a)!=find_parent(parent,b):
      union_parent(parent,a,b)
      #print(a,b)
      #비활성화해도 괜찮은 가로등 비용
      result+=cost
  return (total-result)

if __name__=="__main__":
    v,e=7,11
    #points =  [[0,0],[2,2],[3,10],[5,2],[7,0]]
    #print(make_edges(points))
    edges=[]
    edge=[[0,1,7],[0,3,5],[1,2,8],[1,3,9],[1,4,7],[2,4,5],[3,4,15],[3,5,6],[4,5,8],[4,6,9],[5,6,11]]
    for r in edge:
        a,b,cost=r
        #edges.append((r[2],r[1],r[0]))
        edges.append((r[2],r[0],r[1]))
    print(kruskal(edges,v,e))