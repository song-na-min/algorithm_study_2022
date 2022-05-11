

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
def make_edges(points):
  edges=[]
  n=len(points)
  #print(n)
  j=0
  for i in range(n):
    for j in range(i+1,n):
      dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
      edges.append((dist,i+1,j+1))
      edges.append((dist,j+1,i+1))
  return edges
def kruskal(edges,v):
  #edges=make_edges(points)
  #v=len(points)
  parent=[0]*(v+1)
  result=0
  for i in range(1,v+1):
    parent[i]=i
  edges.sort()
  for edge in edges:
    cost,a,b=edge
    if find_parent(parent,a)!=find_parent(parent,b):
      union_parent(parent,a,b)
      #print(a,b)
      result+=cost
  return result

if __name__=="__main__":
    v=5
    arr=[[11,-15,-15],[14,-5,-15],[-1,-1,-5],[10,-4,-1],[19,-4,-19]]
    #points =  [[0,0],[2,2],[3,10],[5,2],[7,0]]
    #print(make_edges(points))
    edges=[]
    for i in range(v):
        for j in range(i):
            dist=min(abs(arr[i][0]-arr[j][0]),abs(arr[i][1]-arr[j][1]),abs(arr[i][2]-arr[j][2]))
            edges.append([dist,i+1,j+1])
    #print(edges)
    print(kruskal(edges,v))