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
  last=0
  for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
      union_parent(parent,a,b)
      #print(a,b)
      result+=cost
      last=cost
  return (result-last)

if __name__=="__main__":
    v,e=7,12
    #points =  [[0,0],[2,2],[3,10],[5,2],[7,0]]
    #print(make_edges(points))
    edges=[]
    edge=[[1,2,3],[1,3,2],[3,2,1],[2,5,2],[3,4,4],[7,3,6],[5,1,5],[1,6,2],[6,4,1],[6,5,3],[4,5,3],[6,7,4]]
    for r in edge:
        a,b,cost=r
        edges.append((r[2],r[1],r[0]))
    print(kruskal(edges,v,e))