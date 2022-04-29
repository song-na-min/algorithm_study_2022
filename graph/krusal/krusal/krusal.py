
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
def kruskal(edges,v,e):
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
    v,e=7,9
    #points =  [[0,0],[2,2],[3,10],[5,2],[7,0]]
    #print(make_edges(points))
    edges=[
        [29,1,2],
        [75,1,5],
        [35,2,3],
        [34,2,6],
        [7,3,4],
        [23,4,6],
        [13,4,7],
        [53,5,6],
        [25,6,7]]
    print(kruskal(edges,v,e))